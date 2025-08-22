# test_kernel.py
# Interactive version for story input and rule checking

import json
from core.universal_rules import UNIVERSAL_RULES
from core.candidate_rules import CANDIDATE_RULES

# Define meaningless / low-value words
DISCARDED_WORDS = ["it", "these", "from", "that", "at", "other", "over"]

def find_matches(story):
    matches = []
    new_candidates = []
    discarded = []

    story_lower = story.lower()

    # Check universal rules
    for rule in UNIVERSAL_RULES:
        if any(word.lower() in story_lower for word in rule['description'].split()):
            matches.append(rule)

    # Check candidate rules
    for cand in CANDIDATE_RULES:
        if any(word.lower() in story_lower for word in cand['description'].split()):
            if any(word in DISCARDED_WORDS for word in cand['description'].split()):
                discarded.append(cand)
            else:
                new_candidates.append(cand)

    return {
        "story": story,
        "matches": matches,
        "new_candidates": new_candidates,
        "discarded": discarded
    }

def main():
    print("=== Interactive Test Kernel ===")
    print("Type 'exit' to quit.\n")

    while True:
        story = input("Enter a story: ").strip()
        if story.lower() == "exit":
            break

        results = find_matches(story)
        print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()

