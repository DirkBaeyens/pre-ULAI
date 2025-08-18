# File: core/universal_rules.py
# Version: 2025-08-15 15:42
"""
Universal Rules Module
----------------------
Contains the most fundamental and temporary basic logic rules
used by the pre-ULAI system as its core reference layer.
"""

UNIVERSAL_RULES = [
    "Energy is never lost, only transformed or redirected.",
    "Balance in systems leads to stability; imbalance leads to change.",
    "Cold and heat are complementary flows, each enabling the other.",
    "All parts are connected; the whole influences the parts, and vice versa.",
    "Cycles are natural; straight lines are temporary deviations.",
    "Observation is limited by the observer’s tools and position.",
    "Logic must remain open to future input and revision."
]

def get_rules():
    """
    Returns the list of universal rules.
    """
    return UNIVERSAL_RULES

def print_rules():
    """
    Prints the universal rules in a readable format.
    """
    for i, rule in enumerate(UNIVERSAL_RULES, 1):
        print(f"{i}. {rule}")

if __name__ == "__main__":
    print("Universal Logic Rules:")
    print_rules()

