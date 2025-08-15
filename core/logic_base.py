# core/logic_base.py
# Version: 2025-08-15
# Purpose: Stores and recalls universal basic logic rules persistently

import json
import os

RULES_FILE = "core/logic_rules.json"

def load_rules():
    """Load rules from JSON file, or return an empty list if none exist."""
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_rules(rules):
    """Save rules to JSON file."""
    with open(RULES_FILE, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=2, ensure_ascii=False)

def add_rule(rules, new_rule):
    """Add a new rule if it doesn't already exist."""
    if new_rule not in rules:
        rules.append(new_rule)
        print(f"✅ Added rule: {new_rule}")
    else:
        print(f"⚠️ Rule already exists: {new_rule}")
    return rules

def list_rules(rules):
    """Print all rules."""
    if not rules:
        print("No rules stored yet.")
    else:
        print("\n📜 Stored Universal Logic Rules:")
        for idx, rule in enumerate(rules, start=1):
            print(f"{idx}. {rule}")

def main():
    rules = load_rules()

    while True:
        print("\nOptions: [1] List rules  [2] Add rule  [3] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            list_rules(rules)
        elif choice == "2":
            new_rule = input("Enter new universal logic rule: ").strip()
            if new_rule:
                rules = add_rule(rules, new_rule)
                save_rules(rules)
        elif choice == "3":
            save_rules(rules)
            print("💾 Rules saved. Goodbye.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()

