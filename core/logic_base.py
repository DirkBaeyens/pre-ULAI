# File: core/logic_base.py
# Version: 2025-08-15 16:07
"""
Logic Base Module
-----------------
Provides core logical operations for the pre-ULAI system.
Now integrates universal rules as its reference layer.
"""

from core.universal_rules.py import get_rules

class LogicBase:
    def __init__(self):
        self.rules = get_rules()

    def validate_statement(self, statement: str) -> bool:
        """
        Checks if a given statement aligns with the universal rules.
        For now, this is a very basic check (string match).
        Future versions can expand to semantic analysis.
        """
        return any(rule.lower() in statement.lower() for rule in self.rules)

    def explain_alignment(self, statement: str) -> str:
        """
        Provides an explanation of how a statement aligns (or not) with universal rules.
        """
        aligned_rules = [rule for rule in self.rules if rule.lower() in statement.lower()]
        if aligned_rules:
            return f"The statement aligns with {len(aligned_rules)} universal rule(s): {aligned_rules}"
        return "The statement does not align with any universal rules (yet)."

if __name__ == "__main__":
    lb = LogicBase()
    test_statement = "Energy is never lost, only redirected."
    print("Testing statement:", test_statement)
    print("Validation:", lb.validate_statement(test_statement))
    print("Explanation:", lb.explain_alignment(test_statement))

