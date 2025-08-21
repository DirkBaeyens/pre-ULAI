# test_observations.py
# Version: 2025-08-19 22:50

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
        # --- Layer 1: Original rules ---
        "The cause of the storm was rising heat in the ocean.",
        "Water always seeks balance and flows downhill.",
        "Energy transformed into heat during friction.",
        "All species are connected through ecosystems.",
        "Seasons repeat in a cycle each year.",
        "The storm was caused due to heat and followed a repeating seasonal cycle.",
        "This is a random unrelated statement.",

        # --- Layer 2: Expanded rules ---
        # cause_effect expansions
        "The domino effect caused a cascade of failures in the system.",          # chain_reaction
        "The disease spread had a hidden cause we could not observe directly.",   # hidden_cause

        # balance_flow expansions
        "The economy overshot and overcorrected itself after the crash.",         # overcompensation
        "The thermostat works as a feedback loop to regulate temperature.",       # feedback_loop

        # continuity expansions
        "Water transforms into vapor when heated, then condenses back to liquid.",# transformation
        "The battery stored energy during the day and released it at night.",     # storage_release

        # interconnection expansions
        "Bees and flowers live in mutual dependence for survival.",               # mutual_dependence
        "The virus spread indirectly through an intermediary host.",              # indirect_link

        # cycles expansions
        "Civilizations rise and fall in a spiral of growth and decay.",           # spiral_growth
        "Water undergoes a phase transition from liquid to gas at 100°C.",        # phase_transition
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

