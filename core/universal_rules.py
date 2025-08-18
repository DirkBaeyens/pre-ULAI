# core/universal_rules.py
# Version: 2025-08-18 16:30

class UniversalRules:
    def __init__(self):
        self.rules = [
            {
                "id": "cause_effect",
                "description": "Every action has a reaction, even if delayed or hidden.",
                "type": "causality"
            },
            {
                "id": "balance_flow",
                "description": "All flows seek balance; imbalance creates movement until equilibrium is approached.",
                "type": "balance"
            },
            {
                "id": "continuity",
                "description": "Energy and existence do not vanish, they transform or circulate.",
                "type": "conservation"
            },
            {
                "id": "interconnection",
                "description": "Everything is linked with everything else, directly or indirectly.",
                "type": "relation"
            },
            {
                "id": "cycles",
                "description": "The universe evolves in cycles, not as a one-time event.",
                "type": "time"
            }
        ]

    def list_rules(self):
        return self.rules

