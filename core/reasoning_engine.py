# core/reasoning_engine.py
# Version: 2025-08-18 15:30

from core.universal_rules import rules

class ReasoningEngine:
    def __init__(self):
        self.rules = rules

    def list_rules(self):
        """Return all loaded rules with their descriptions."""
        return [(r["name"], r["description"]) for r in self.rules]

    def apply_rules(self, observation):
        """
        Apply universal rules to an observation.
        Returns a list of insights based on matching rules.
        """
        insights = []
        for rule in self.rules:
            # Simple logic: if a keyword in observation matches a rule name or description, note it
            if rule["name"].lower() in observation.lower() or any(
                kw.lower() in observation.lower() for kw in rule.get("keywords", [])
            ):
                insights.append(f"Rule '{rule['name']}' applies: {rule['description']}")
        return insights

    def reason(self, observation):
        """
        Generate reasoning output for an observation.
        Currently a basic match-based reasoning.
        """
        insights = self.apply_rules(observation)
        if not insights:
            insights.append("No direct universal rule applies, further exploration needed.")
        return insights


# Test block
if __name__ == "__main__":
    engine = ReasoningEngine()
    print("Loaded Rules:")
    for name, desc in engine.list_rules():
        print(f"- {name}: {desc}")

    test_obs = "Observing natural cycles and cause-effect patterns"
    print("\nReasoning on test observation:")
    for insight in engine.reason(test_obs):
        print(f"- {insight}")

