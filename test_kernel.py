# test_kernel.py
# Version: 2025-08-22 22:30
"""
Interactive kernel with persistent memory.

- Input stories interactively (type 'exit' to quit).
- Matches against core/universal_rules.py and core/candidate_rules.py.
- Generates new candidate rules from meaningful, uncovered words.
- Persists:
    - stories.json     -> every story + matches + new candidates + timestamp
    - candidates.json  -> all auto-generated candidates (deduplicated)

Run from project root (folder that contains the 'core' package):
    python3 test_kernel.py
"""

import json
import os
import re
from datetime import datetime

# --- Project imports (expect to run from project root) ---
from core.universal_rules import UNIVERSAL_RULES
from core.candidate_rules import CANDIDATE_RULES as PY_CANDIDATES

# --- Files for persistence (created next to this script) ---
STORIES_FILE = "stories.json"
CANDIDATES_FILE = "candidates.json"

# --- Stopwords / low-meaning tokens ---
STOPWORDS = {
    "a","an","the","and","or","but","if","then","else",
    "to","of","in","on","at","by","for","from","with","without",
    "is","are","was","were","be","been","being",
    "it","this","that","these","those","there","here",
    "as","so","not","no","yes","do","does","did",
    "up","down","over","under","into","out","than","too","very",
    "you","we","they","he","she","i",
    "my","your","their","our","his","her","its"
}

# --- Minimal helpers for persistence ---
def _load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            # If file is corrupt, back it up and start fresh
            try:
                os.rename(path, path + ".bak")
            except Exception:
                pass
    return default

def _save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    os.replace(tmp, path)

# --- Text utils ---
TOKEN_RE = re.compile(r"[A-Za-z0-9_-]+")

def tokenize(text: str):
    # lowercase, keep letters/numbers/_/-, split on others
    return TOKEN_RE.findall(text.lower())

def meaningful_tokens(text: str):
    return [t for t in tokenize(text) if t not in STOPWORDS and len(t) >= 3]

# Build a quick lookup of words present in existing rules (ids + descriptions)
def build_rule_index(rules):
    idx = {}
    for r in rules:
        words = set(meaningful_tokens(r.get("id","")) + meaningful_tokens(r.get("description","")))
        idx[r["id"]] = words
    return idx

def overlap_score(story_tokens_set, rule_words_set):
    # simple score = count of overlapping meaningful tokens
    return len(story_tokens_set & rule_words_set)

# --- Candidate generation heuristics ---
def generate_candidate_ids_from_tokens(tokens, existing_ids):
    """
    Create simple single-word candidate ids for tokens not covered.
    Avoid duplicates and very generic tokens.
    """
    candidates = []
    for t in tokens:
        cid = f"cand_{t}"
        if cid in existing_ids:
            continue
        # Skip ultra-generic tokens that slipped through (tune as needed)
        if t.isdigit() or len(t) < 3:
            continue
        candidates.append(cid)
    return candidates

def guess_cluster_for_token(t):
    if t in {"cycle","cycles","wave","waves","phase","pattern","patterns"}:
        return "Cycles & Waves"
    if t in {"balance","equilibrium","extreme","extremes"}:
        return "Balance & Extremes"
    if t in {"energy","matter","mass","field","flow","flows","current"}:
        return "Matter & Energy"
    if t in {"link","links","interconnect","interconnection","relation"}:
        return "Interconnection"
    if t in {"cause","effect","trigger","cascade"}:
        return "Causality"
    if t in {"store","storage","release","transform","transition"}:
        return "Conservation"
    if t in {"civilization","civilizations","society","societies"}:
        return "Systems"
    return "Unclustered"

def make_candidate_record(cid, token, story_text):
    # readable description template
    desc = f"Candidate rule related to '{token}'."
    return {
        "id": cid,
        "description": desc,
        "origin_story": story_text,
        "status": "candidate",
        "cluster": guess_cluster_for_token(token)
    }

# --- Load current persistent sets ---
def load_candidates_store():
    # Merge Python candidates (static) with JSON-generated candidates (dynamic)
    json_candidates = _load_json(CANDIDATES_FILE, [])
    # Build dict by id to dedupe
    merged = {c["id"]: c for c in PY_CANDIDATES}
    for c in json_candidates:
        merged[c["id"]] = c
    return list(merged.values())

def save_candidates_store(all_candidates):
    # Only save the dynamic part (not the Python file ones).
    # Strategy: keep anything not in PY_CANDIDATES by id.
    py_ids = {c["id"] for c in PY_CANDIDATES}
    dynamic = [c for c in all_candidates if c["id"] not in py_ids]
    _save_json(CANDIDATES_FILE, dynamic)

# --- Core analysis ---
def analyze_story(story_text: str):
    # Load fresh candidates (merged static+dynamic)
    all_candidates = load_candidates_store()

    # Build rule index for universal + candidate
    all_rules = UNIVERSAL_RULES + all_candidates
    rule_index = build_rule_index(all_rules)

    story_tokens = meaningful_tokens(story_text)
    story_set = set(story_tokens)

    # Match & score
    matches = []
    for r in all_rules:
        rid = r["id"]
        score = overlap_score(story_set, rule_index[rid])
        if score > 0:
            matches.append({
                "id": rid,
                "type": r.get("type","candidate"),
                "description": r.get("description",""),
                "score": score
            })

    # Sort matches: highest score first, then universal over candidate
    def sort_key(m):
        # universal rules should typically have types like causality/balance/... (not 'candidate')
        is_universal = 0 if m["type"] in {"causality","balance","conservation","relation","time","hybrid","hidden"} else 1
        return ( -m["score"], is_universal, m["id"] )
    matches.sort(key=sort_key)

    # Determine uncovered tokens (not present in any matched rule words)
    covered_words = set()
    for m in matches:
        covered_words |= rule_index[m["id"]]
    uncovered = [t for t in story_tokens if t not in covered_words]

    # Propose simple new candidates from uncovered tokens
    existing_ids = {r["id"] for r in all_rules}
    new_candidate_ids = generate_candidate_ids_from_tokens(uncovered, existing_ids)
    new_candidates = [make_candidate_record(cid, cid.replace("cand_",""), story_text) for cid in new_candidate_ids]

    # Update dynamic candidates store (append new ones, dedup by id)
    if new_candidates:
        current = load_candidates_store()
        existing = {c["id"]: c for c in current}
        for nc in new_candidates:
            existing[nc["id"]] = nc
        save_candidates_store(list(existing.values()))

    # Persist story log entry
    stories = _load_json(STORIES_FILE, [])
    stories.append({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "story": story_text,
        "matches": matches,
        "new_candidates": new_candidates
    })
    _save_json(STORIES_FILE, stories)

    # Prepare concise, human-friendly summary
    top_matches = [m["id"] for m in matches[:8]]
    summary = {
        "saved_to": {
            "stories": STORIES_FILE,
            "candidates": CANDIDATES_FILE
        },
        "top_matches": top_matches,
        "new_candidates_count": len(new_candidates),
        "new_candidates_sample": [c["id"] for c in new_candidates[:8]]
    }
    return summary

# --- CLI loop ---
def main():
    print("=== pre-ULAI Interactive Kernel ===")
    print("Type a story and press Enter. Type 'exit' to quit.\n")

    while True:
        try:
            story = input("Story> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if story.lower() in {"exit","quit"} or story == "":
            print("Bye.")
            break

        summary = analyze_story(story)
        print("\nSaved ✅")
        print(f"- Stories log: {summary['saved_to']['stories']}")
        print(f"- Candidates:  {summary['saved_to']['candidates']}")
        print(f"- Top matches: {', '.join(summary['top_matches']) if summary['top_matches'] else '(none)'}")
        if summary["new_candidates_count"]:
            print(f"- New candidates: {summary['new_candidates_count']} "
                  f"(e.g., {', '.join(summary['new_candidates_sample'])})")
        else:
            print("- New candidates: 0")
        print("")

if __name__ == "__main__":
    main()

