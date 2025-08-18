# File: core/reasoning_engine.py
# Version: 2025-08-18 10:07
"""
Reasoning Engine
----------------
Takes inputs (ideas/statements) and evaluates them against the universal rules.
Returns:
- alignment score (0..1)
- matched rules
- missing themes (gaps)
- a suggested refinement that better aligns with the universal logic core
"""

from typing import Dict, List
from core.logic_base import LogicBase


# Lightweight themes we expect in universal logic; used to detect "gaps".
THEMES = {
    "energy": ["energy", "heat", "hot", "fire", "radiate", "outflow", "emit", "transform"],
    "matter": ["matter", "mass", "cold", "fuel", "inflow", "absorb", "accrete", "condense"],
    "balance": ["balance", "harmony", "equilibrium", "stability", "counter", "opposition"],
    "cycles": ["cycle", "cyclic", "periodic", "feedback", "loop", "return", "flow"],
    "connection": ["connected", "interlinked", "interdependent", "whole", "network", "system"],
    "scale": ["micro", "macro", "scale", "fractal", "nested", "hierarchy"],
    "change": ["transform", "evolve", "adapt", "phase", "transition", "convert"],
}


class ReasoningEngine:
    def __init__(self):
        self.logic = LogicBase()
        self.rules = self.logic.all_rules()

    def _theme_hits(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        return {k: any(word in t for word in words) for k, words in THEMES.items()}

    def evaluate(self, statement: str) -> Dict:
        """
        Evaluate a statement against universal rules and themes.
        """
        matched = self.logic.matched_rules(statement)
        theme_hits = self._theme_hits(statement)

        # Alignment score: combine explicit rule matches + theme coverage
        rule_score = len(matched) / max(1, len(self.rules))
        theme_score = sum(theme_hits.values()) / max(1, len(THEMES))
        alignment = round(0.5 * rule_score + 0.5 * theme_score, 3)

        gaps = [theme for theme, hit in theme_hits.items() if not hit]

        return {
            "statement": statement,
            "alignment_score": alignment,            # 0..1
            "matched_rules": matched,                # which universal rules it echoes explicitly
            "theme_coverage": theme_hits,            # which core themes appear
            "gaps": gaps,                            # missing universal themes
            "explanation": self.logic.explain_alignment(statement),
        }

    def suggest_refinement(self, statement: str, eval_result: Dict) -> str:
        """
        Propose a refined sentence that incorporates missing themes
        without changing the author's intended meaning.
        """
        base = statement.strip()
        if not base.endswith("."):
            base += "."

        additions: List[str] = []

        # Nudge towards missing themes
        if "energy" in eval_result["gaps"]:
            additions.append("It acknowledges outward energy flow and transformation")
        if "matter" in eval_result["gaps"]:
            additions.append("it accounts for inward matter accretion and condensation")
        if "balance" in eval_result["gaps"]:
            additions.append("it preserves systemic balance across opposing forces")
        if "cycles" in eval_result["gaps"]:
            additions.append("it operates within cyclic feedback rather than one-off events")
        if "connection" in eval_result["gaps"]:
            additions.append("it remains interconnected with the larger whole")
        if "scale" in eval_result["gaps"]:
            additions.append("it holds consistently from micro to macro scales")
        if "change" in eval_result["gaps"]:
            additions.append("it allows adaptive transformation over time")

        if additions:
            tail = "; ".join(additions) + "."
            return f"{base} In this framing, {tail}"
        else:
            return base  # already good

    def analyze(self, statement: str) -> Dict:
        """
        Full pipeline: evaluate + propose refinement.
        """
        result = self.evaluate(statement)
        result["suggested_refinement"] = self.suggest_refinement(statement, result)
        return result

