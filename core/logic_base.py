# logic_base.py
# Version: 2025-08-15
# This file contains the core universal basic logic rules for the Pre-ULAI project.

from datetime import datetime

class LogicBase:
    """
    A foundational class to hold and evaluate basic universal logic rules.
    """

    def __init__(self):
        self.rules = []
        self.created_at = datetime.utcnow()

    def add_rule(self, description: str):
        """
        Add a new basic logic rule to the system.
        """
        self.rules.append({
            "description": description,
            "added_at": datetime.utcnow()
        })

    def list_rules(self):
        """
        Return a list of all stored rules.
        """
        return self.rules

    def evaluate_rule(self, index: int):
        """
        Placeholder for evaluating a rule.
        For now, it simply returns the rule description.
        """
        if 0 <= index < len(self.rules):
            return self.rules[index]["description"]
        else:
            return "Rule index out of range."

if __name__ == "__main__":
    lb = LogicBase()
    
    # Example rules from our universal logic discussion
    lb.add_rule("Energy flows outward from a core; matter flows inward from surroundings.")
    lb.add_rule("Hot fire and cold fuel form a continuous interaction cycle.")
    lb.add_rule("The universe operates on gradual, cyclic transformations, not a single starting point.")
    
    print(f"Logic Base created at: {lb.created_at}")
    print("Current Universal Basic Rules:")
    for i, rule in enumerate(lb.list_rules()):
        print(f"{i+1}. {rule['description']}")

