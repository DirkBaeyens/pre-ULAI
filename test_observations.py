# test_observations.py
# Version: 2025-08-20 00:25
"""
Test Observations
-----------------
Runs text inputs through the ReasoningEngine to see which universal rules
are triggered. Now also tests hybrid rule activations.
"""

from core.reasoning_engine import ReasoningEngine


def run_tests():
    engine = ReasoningEngine()

    test_cases = [
        # Base rules
        "Every action causes a reaction, and sometimes hidden causes appear.",
        "Flows always move toward balance, but sometimes overshoot the goal.",
        "Energy does not vanish, it only transforms and circulates in cycles.",
        "Everything is connected, even indirectly through hidden links.",
        "Time repeats itself in cycles, sometimes spiraling forward.",

        # Hybrid triggers
        "One event sparks another, creating a chain reaction, but balance is also restored.",
        "Energy is stored and then released, making cycles stronger over time.",
        "Things depend on each other, and together they spiral into new growth.",
    ]

    for i, text in enumerate(test_cases, 1):
        activated = engine.analyze(text)
        print(f"\nTest {i}: {text}")
        for rule in activated:
            print(f" - {rule['id']}: {rule['description']} (type: {rule['type']})")


if __name__ == "__main__":
    run_tests()

