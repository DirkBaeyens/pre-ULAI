# core/reasoning_engine.py
# Version: 2025-08-18 16:50

from core.universal_rules import UniversalRules

class ReasoningEngine:
    def __init__(self):
        self.rules = UniversalRules().list_rules()
        self.observations = []

    def add_observation(self, observation):
        """
        Add a new observation to the reasoning engine.
        Each observation should be a dictionary with keys like 'id', 'description', 'type'.
        """
        self.observations.append(observation)

    def analyze(self):
        """
        Basic analysis: match observations to universal rules.
        Returns a list of tuples (observation_id, matched_rule_id).
        """
        results = []
        for obs in self.observations:
            matched_rules = []
            for rule in self.rules:
                if rule['type'] == obs.get('type'):
                    matched_rules.append(rule['id'])
            results.append({
                "observation_id": obs.get("id"),
                "matched_rules": matched_rules
            })
        return results

