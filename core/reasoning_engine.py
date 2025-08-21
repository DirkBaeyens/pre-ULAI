# core/reasoning_engine.py
# Version: 2025-08-19 21:40

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
            score, hits = self._match_score(obs_text, rule)
            if score > 0:
                results.append({
                    "rule_id": rule["id"],
                    "description": rule["description"],
                    "match": True,
                    "confidence": round(score, 2),
                    "hits": hits,
                    "explanation": f"Observation relates to '{rule['id']}' ({rule['type']})."
                })

        return {
            "observation": observation,
            "matches": results if results else [{"match": False, "explanation": "No universal rule matched."}]
        }

    def _match_score(self, obs_text, rule):
        """
        Improved matcher with scoring.
        Returns (score, hits).
        """
        keyword_map = {
            "cause_effect": ["cause", "effect", "because", "due to", "trigger", "reaction"],
            "balance_flow": ["balance", "flow", "equilibrium", "stability", "adjust", "restore"],
            "continuity": ["energy", "transform", "circulate", "change", "convert", "conserve"],
            "interconnection": ["connected", "relation", "link", "interaction", "network", "web"],
            "cycles": ["cycle", "repeat", "pattern", "recurring", "loop", "season", "rotation"]
        }

        hits = []
        score = 0

        for kw in keyword_map.get(rule["id"], []):
            if kw in obs_text:
                hits.append(kw)
                score += 1

        # Normalize score (0.0 – 1.0 scale)
        if hits:
            score = score / len(keyword_map[rule["id"]])
        return score, hits

