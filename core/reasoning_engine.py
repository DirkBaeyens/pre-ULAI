# core/reasoning_engine.py
# Version: 2025-08-19 23:30

"""
Reasoning Engine
----------------
Applies universal rules to given observations.
Now also aware of kernel and candidate rules.
"""

from core.universal_rules import UNIVERSAL_RULES
from core.rule_registry import KERNEL_RULES, CANDIDATE_RULES


class ReasoningEngine:
    def __init__(self):
        self.kernel_rules = {rule["id"]: rule for rule in UNIVERSAL_RULES if rule["id"] in KERNEL_RULES}
        self.candidate_rules = {rule["id"]: rule for rule in CANDIDATE_RULES}

    def apply_rules(self, observation: str):
        """
        Apply kernel rules to an observation and annotate candidate awareness.
        """
        results = []

        # --- Apply kernel rules ---
        for rule_id, rule in self.kernel_rules.items():
            if rule["id"] in observation or any(word in observation for word in rule["description"].split()):
                results.append({
                    "rule": rule["id"],
                    "type": "kernel",
                    "explanation": f"Matched kernel rule '{rule['id']}' → {rule['description']}"
                })

        # --- Awareness of candidate rules ---
        candidate_refs = []
        for rule_id, rule in self.candidate_rules.items():
            if rule["id"] in observation or any(word in observation for word in rule["description"].split()):
                candidate_refs.append(rule_id)

        if candidate_refs:
            results.append({
                "rule": "candidate_reference",
                "type": "candidate",
                "explanation": f"Observation hints at candidate rules: {', '.join(candidate_refs)}"
            })

        if not results:
            results.append({
                "rule": "none",
                "type": "unknown",
                "explanation": "No clear kernel rule matched. Candidate awareness noted."
            })

        return results

