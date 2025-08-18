# File: main.py
# Version: 2025-08-18 10:09
"""
pre-ULAI quick CLI
Type a statement and see how it aligns with universal rules,
which themes are missing, and a suggested refinement.
"""

from core.reasoning_engine import ReasoningEngine

def pretty(d: dict):
    print("\n--- Analysis ---")
    print(f"Statement: {d['statement']}")
    print(f"Alignment Score: {d['alignment_score']}")
    print(f"Matched Rules: {d['matched_rules']}")
    print(f"Themes: {d['theme_coverage']}")
    print(f"Gaps: {d['gaps']}")
    print(f"Explanation: {d['explanation']}")
    print("\nSuggested Refinement:")
    print(d["suggested_refinement"])
    print("------------------\n")

if __name__ == "__main__":
    engine = ReasoningEngine()
    print("pre-ULAI Reasoning CLI — type 'exit' to quit.")
    while True:
        s = input("\nEnter a statement: ").strip()
        if s.lower() in {"exit", "quit"}:
            break
        result = engine.analyze(s)
        pretty(result)

