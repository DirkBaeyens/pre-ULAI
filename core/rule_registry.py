# core/rule_registry.py
# Version: 2025-08-19 23:05

"""
Rule Registry
-------------
This file maintains structured lists of:
1. Active Kernel Rules (confirmed in universal_rules.py)
2. Candidate Rules (prepared for future integration)

These registries allow the system to keep track of
core stability while leaving space for gradual evolution.
"""

# --- 1. Kernel Rules (as of 2025-08-19) ---
KERNEL_RULES = [
    "cause_effect",
    "balance_flow",
    "continuity",
    "interconnection",
    "cycles",
    "cause_balance",
    "continuity_interconnection",
    "cycles_balance",
    "pair_rule_1",
    "pair_rule_2",
]

# --- 2. Candidate Rules (future expansion) ---
CANDIDATE_RULES = [
    {"id": "symmetry", "description": "Phenomena appear in mirrored or complementary pairs."},
    {"id": "threshold", "description": "Small changes accumulate until a tipping point triggers transformation."},
    {"id": "feedback", "description": "Outputs can loop back as inputs, strengthening or weakening cycles."},
    {"id": "emergence", "description": "Complex patterns arise from simple interactions without central control."},
    {"id": "local_global", "description": "Local behavior can differ from global outcomes, but both are linked."},
    {"id": "pair_rule_3", "description": "Reserved hidden rule slot."},
    {"id": "pair_rule_4", "description": "Reserved hidden rule slot."}
]

