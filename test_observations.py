# test_observations.py
# Version: 2025-08-19 23:45

"""
Test Observations
-----------------
Run sample observations through the ReasoningEngine.
Now also checks for candidate rule awareness.
"""

from core.reasoning_engine import ReasoningEngine

engine = ReasoningEngine()

# Define test observations
OBSERVATIONS = [
    # Kernel rule triggers
    "If you push something, it pushes back because every action has a reaction.",
    "Heat moves from hot to cold until balance is reached.",
    "Nothing disappears, energy circulates instead of vanishing.",
    "The Earth and Moon are interconnected through gravity.",
    "Seasons repeat in cycles over time.",

    # Candidate rule hints
    "The human body is symmetric, left and right mirror each other.",
    "Systems often return feedback that stabilizes them.",
    "Small causes can trigger large effects like avalanches.",
    "Patterns emerge when simple rules combine.",
    "Some interactions seem hidden but influence outcomes.",

    # Unknown case
    "A cat jumps over the fence."
]

print("\n--- Running Observations through ReasoningEngine ---\n")
for obs in OBSERVATIONS:
    print(f"Observation: {obs}")
    results = engine.apply_rules(obs)
    for r in results:
        print(f"  - [{r['type']}] {r['explanation']}")
    print()

