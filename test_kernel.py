# test_kernel.py
# Version: 2025-08-22
"""
Test Harness for Universal Rules
--------------------------------
Takes a story or description and checks it against the universal rules.
"""

import re
from core.universal_rules import UNIVERSAL_RULES

def match_rules(story: str):
    """
    Match a story against the universal rules.
    Returns a report of which rules matched, conflicts, and gaps.
    """
    story_lower = story.lower()
    matched = []
    candidates = []

    # Simple keyword map (expandable later)
    keyword_map = {
        "cause_effect": ["cause", "effect", "reaction", "trigger"],
        "balance_flow": ["balance", "equilibrium", "flow", "imbalance"],
        "continuity": ["transform", "circulate", "convert", "does not vanish"],
        "interconnection": ["link", "connected", "relation", "network"],
        "cycles": ["cycle", "repeat", "oscillate", "return"],

        # Expanded
        "chain_reaction": ["cascade", "chain", "domino"],
        "hidden_cause": ["hidden", "invisible", "unknown", "unseen"],
        "overcompensation": ["swing", "overshoot"],
        "feedback_loop": ["feedback", "loop", "self regulate"],
        "transformation": ["change", "transform", "convert"],
        "storage_release": ["store", "release", "build up"],
        "mutual_dependence": ["depend", "support each other"],
        "indirect_link": ["indirect", "via", "through"],
        "spiral_growth": ["spiral", "evolve", "growth"],
        "phase_transition": ["threshold", "phase", "sudden change"],

        # Completion
        "cycle_completion": ["complete cycle", "close loop", "full circle"],
        "waveform_completeness": ["wave", "peak", "trough", "amplitude"],
        "balance_between_extremes": ["opposite", "extreme", "middle", "balance"],
    }

    for rule in UNIVERSAL_RULES:
        rid = rule["id"]
        if rid in keyword_map:
            for kw in keyword_map[rid]:
                if kw in story_lower:
                    matched.append(rule)
                    break

    # Detect conflicts (simple example: story says "vanish" → violates continuity)
    conflicts = []
    if "vanish" in story_lower or "disappear" in story_lower:
        conflicts.append("continuity")

    return {
        "matched": matched,
        "conflicts": conflicts,
        "candidates": candidates
    }

if __name__ == "__main__":
    story = input("Enter your story: ")
    result = match_rules(story)

    print("\n=== Test Kernel Report ===")
    print("\nMatched Rules:")
    for r in result["matched"]:
        print(f" - {r['id']}: {r['description']}")

    if result["conflicts"]:
        print("\nConflicts Found:")
        for c in result["conflicts"]:
            print(f" - Conflict with rule: {c}")

    if result["candidates"]:
        print("\nNew Candidate Ideas:")
        for c in result["candidates"]:
            print(f" - {c}")

    print("\nDone.")

