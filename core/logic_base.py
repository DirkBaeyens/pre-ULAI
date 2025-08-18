# File: core/logic_base.py
# Version: 2025-08-18 10:05
"""
Logic Base Module
-----------------
Provides core logical operations for the pre-ULAI system.
Integrates universal rules as its reference layer.
"""

from typing import List
from core.universal_rules import get_rules


class LogicBase:
    def __init__(self):
        self.rules: List[str] = get_rules()

    def all_rules(self) -> List[str]:
        return list(self.rules)

    def validate_statement(self, statement: str) -> bool:
        """
        Basic alignment check: does the statement explicitly touch any universal rule?
        """
        s = statement.lower()
        return any(rule.lower() in s for rule in self.rules)

    def matched_rules(self, statement: str) -> List[str]:
        s = statement.lower()
        return [rule for rule in self.rules if rule.lower() in s]

    def explain_alignment(self, statement: str) -> str:
        aligned = self.matched_rules(statement)
        if aligned:
            return f"The statement aligns with {len(aligned)} universal rule(s): {aligned}"
        return "The statement does not explicitly align with any universal rules yet."

