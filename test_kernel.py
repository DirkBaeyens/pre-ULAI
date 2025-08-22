# test_kernel.py
# Version: 2025-08-22
import json
from core.universal_rules import UNIVERSAL_RULES
from core.candidate_rules import CANDIDATE_RULES

# Keywords extracted from candidate rules (simple for now)
KEYWORDS = [c["id"].replace("cand_", "").replace("_rule", "") for c in CANDIDATE_RULES]

def match_rules(story_text):
    story_words = story_text.lower().split()
    matches = []
    new_candidates = []

    # Check universal rules
    for rule in UNIVERSAL_RULES:
        for kw in story_words:
            if kw in rule["description"].lower() or kw in rule["id"]:
                matches.append(rule)
                break

    # Check candidate rules
    cluster_matches = {}
    for candidate in CANDIDATE_RULES:
        candidate_id = candidate["id"]
        cluster = candidate.get("cluster", "Unclustered")
        if any(kw in story_words for kw in candidate_id.lower().split("_")):
            if cluster not in cluster_matches:
                cluster_matches[cluster] = []
            cluster_matches[cluster].append(candidate)

    return matches, cluster_matches, new_candidates

def interactive_input():
    print("Enter your story (or 'quit' to exit):")
    while True:
        story_text = input("> ")
        if story_text.lower() in ("quit", "exit"):
            break

        matches, cluster_matches, new_candidates = match_rules(story_text)

        print("\n=== Universal Rule Matches ===")
        for m in matches:
            print(f"- {m['id']}: {m['description']} [{m['type']}]")

        print("\n=== Candidate Rule Matches (clustered) ===")
        for cluster, candidates in cluster_matches.items():
            print(f"\n--- Cluster: {cluster} ---")
            for c in candidates:
                print(f"- {c['id']}: {c['description']} [status: {c['status']}]")

        if new_candidates:
            print("\n=== New Candidate Suggestions ===")
            for nc in new_candidates:
                print(f"- {nc['description']}")

        print("\nEnter next story or 'quit' to exit:")

if __name__ == "__main__":
    interactive_input()

