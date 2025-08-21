# core/reasoning_engine.py
# Version: 2025-08-20 00:05
"""
Reasoning Engine
----------------
Loads universal rules and applies reasoning to input text.
Now supports:
- Keyword-based matching for explicit rules.
- Hybrid rule activation when parent rules are both triggered.
- Hidden rules remain dormant unless explicitly linked in the future.
"""

import re
from core.universal_rules import UNIVERSAL_RULES


class ReasoningEngine:
    def __init__(self):
        self.rules = UNIVERSAL_RULES
        # Index for easier lookup
        self.rule_dict = {rule["id"]: rule for rule in self.rules}

    def analyze(self, text):
        """
        Analyze input text and return matching rules and hybrid activations.
        """
        text = text.lower()
        activated = []

        # Step 1: Match by keyword from description
        for rule in self.rules:
            if rule["type"] in ["hidden", "hybrid"]:
                continue  # Skip hidden/hybrids in keyword search
            keywords = re.findall(r"\w+", rule["description"].lower())
            if any(kw in text for kw in keywords if len(kw) > 4):  # ignore very short words
                activated.append(rule["id"])

        # Step 2: Trigger hybrid rules based on parent references
        for rule in self.rules:
            if rule["type"] != "hybrid":
                continue
            # description format: "Cross-rule: parentA × parentB."
            if "×" in rule["description"]:
                parents = [p.strip() for p in rule["description"].split("×")]
                if len(parents) == 2:
                    if parents[0] in activated and parents[1] in activated:
                        activated.append(rule["id"])

        # Deduplicate
        activated = list(set(activated))

        # Step 3: Return rule details
        return [self.rule_dict[rid] for rid in activated]

