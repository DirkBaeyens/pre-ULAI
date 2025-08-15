# engine.py
from core_rules import CoreRules

class Engine:
    def __init__(self):
        self.rules = CoreRules()

    def run_cycle(self, steps=5):
        print("Running pre-ULAI engine cycles...")
        for step in range(steps):
            output = self.rules.basic_cycle()
            print(f"Cycle {step+1}: output={output}")

if __name__ == "__main__":
    engine = Engine()
    engine.run_cycle()

