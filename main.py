# main.py
# Version: 2025-08-18 15:50

from core.reasoning_engine import ReasoningEngine

def main():
    engine = ReasoningEngine()
    print("=== Pre-AI Reasoning System ===")
    print("Type 'exit' to quit.\n")

    while True:
        observation = input("Enter an observation: ").strip()
        if observation.lower() == "exit":
            print("Exiting reasoning system.")
            break

        insights = engine.reason(observation)
        print("\nInsights:")
        for insight in insights:
            print(f"- {insight}")
        print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    main()

