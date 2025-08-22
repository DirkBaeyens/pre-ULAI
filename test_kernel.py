# core/test_kernel.py
# Version: 2025-08-22 20:45

import json
from core.universal_rules import UNIVERSAL_RULES
from core.candidate_rules import CANDIDATE_RULES

# Stopwords to ignore in story matching
STOPWORDS = ["it", "these", "from", "at", "that", "other", "a", "an", "the", "is", "are"]

def extract_keywords(story):
    """Simple keyword extraction: lowercase, split, remove stopwords"""
    words = story.lower().replace(".", "").replace(",", "").split()
    keywords = [w for w in words if w not in STOPWORDS]
    return set(keywords)

def check_story(story):
    keywords = extract_keywords(story)

    matches = []
    new_candidates = []
    discarded = []

    # Check universal rules
    for rule in UNIVERSAL_RULES:
        rule_words = set(rule["description"].lower().split())
        rule_keywords = rule_words - set(STOPWORDS)
        if keywords & rule_keywords:
            matches.append(rule)

    # Check candidate rules
    for rule in CANDIDATE_RULES:
        rule_words = set(rule["description"].lower().split())
        rule_keywords = rule_words - set(STOPWORDS)
        if keywords & rule_keywords:
            if rule_keywords:
                new_candidates.append(rule)
            else:
                # Only meaningless words matched
                rule_copy = rule.copy()
                rule_copy["status"] = "discarded"
                discarded.append(rule_copy)

    result = {
        "story": story,
        "matches": matches,
        "new_candidates": new_candidates,
        "discarded": discarded
    }

    return result

if __name__ == "__main__":
    # Example story for testing
    story_input = "A lightning needs grounding to release energy."
    result = check_story(story_input)
    print(json.dumps(result, indent=4))

