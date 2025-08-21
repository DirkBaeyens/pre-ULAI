# core/reasoning_engine.py
# Version: 2025-08-19 21:10

"""
Reasoning Engine
----------------
This module applies universal reasoning rules to input observations.
"""

from core.universal_rules import UNIVERSAL_RULES

class ReasoningEngine:
    def __init__(self):
        self.rules = UNIVERSAL_RULES

    def apply_rules(self, observation):
        """
        Apply universal rules to a given observation.
        
        Parameters:
            observation (str or dict): Input observation.
        
        Returns:
            dict: reasoning trace with matched rules and explanations.
        """
        obs_text = str(observation).lower()
        results = []

        for rule in self.rules:
            if self._matches_rule(obs_text, rule):
                results.append({
                    "rule_id": rule["id"],
                    "description": rule["description"],
                    "match": True,
                    "explanation": f"Observation relates to '{rule['id']}' ({rule['type']})."
                })

        return {
            "observation": observation,
            "matches": results if results else [{"match": False, "explanation": "No universal rule matched."}]
        }

    def _matches_rule(self, obs_text, rule):
        """
        Simple heuristic matcher for rules.
        (Temporary until symbolic/semantic reasoning is added.)
        """
        keywords = {
            "cause_effect": ["cause", "effect", "because", "reaction"],
            "balance_flow": ["balance", "flow", "equilibrium", "stability"],
            "continuity": ["energy", "transform", "circulate", "change"],
            "interconnection": ["connected", "relation", "link", "interaction"],
            "cycles": ["cycle", "repeat", "pattern", "recurring", "loop"]
        }
        for kw in keywords.get(rule["id"], []):
            if kw in obs_text:
                return True
        return False

