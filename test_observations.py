# test_observations.py
# Version: 2025-08-19 21:55

"""
Test Observations for ReasoningEngine
-------------------------------------
This script runs example observations through the ReasoningEngine
and prints reasoning traces with confidence scores.
"""

from core.reasoning_engine import ReasoningEngine

def run_tests():
    engine = ReasoningEngine()

    observations = [
        "The cause of the storm was rising heat in the ocean.",
        "Water always seeks balance and flows downhill.",
        "Energy transformed into heat during friction.",
        "All species are connected through ecosystems.",
        "Seasons repeat in a cycle each year.",
        "The storm was caused due to heat and followed a repeating seasonal cycle.",
        "This is a random unrelated statement."
    ]

    for obs in observations:
        result = engine.apply_rules(obs)
        print("\nObservation:", obs)
        for match in result["matches"]:
            if match["match"]:
                print(f" - Rule: {match['rule_id']} ({match['description']})")
                print(f"   Confidence: {match['confidence']}")
                print(f"   Hits: {match['hits']}")
            else:
                print(" -", match["explanation"])

if __name__ == "__main__":
    run_tests()

