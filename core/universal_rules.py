# core/universal_rules.py
# Version: 2025-08-19 22:20
"""
Universal Basic Logic Rules
---------------------------
This file defines the fundamental logic rules for the pre-ULAI project.
These are not scientific laws but simple universal reasoning seeds.

Layer 1 → Root rules (5)
Layer 2 → Expanded rules (10)
"""

UNIVERSAL_RULES = [
    # --- Layer 1: Root Rules ---
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
    },

    # --- Layer 2: Expanded Rules ---
    # From cause_effect
    {
        "id": "chain_reaction",
        "description": "One effect can become the cause of the next, forming cascades.",
        "type": "causality"
    },
    {
        "id": "hidden_cause",
        "description": "Causes may exist outside direct observation, but still shape outcomes.",
        "type": "causality"
    },

    # From balance_flow
    {
        "id": "overcompensation",
        "description": "Systems can swing too far when trying to restore balance.",
        "type": "balance"
    },
    {
        "id": "feedback_loop",
        "description": "Flows often self-regulate through reinforcing or damping effects.",
        "type": "balance"
    },

    # From continuity
    {
        "id": "transformation",
        "description": "Forms of energy or existence shift but maintain essence.",
        "type": "conservation"
    },
    {
        "id": "storage_release",
        "description": "Continuity often involves storing energy and later releasing it.",
        "type": "conservation"
    },

    # From interconnection
    {
        "id": "mutual_dependence",
        "description": "Entities sustain each other’s existence through cooperation.",
        "type": "relation"
    },
    {
        "id": "indirect_link",
        "description": "Things may influence one another through intermediaries.",
        "type": "relation"
    },

    # From cycles
    {
        "id": "spiral_growth",
        "description": "Cycles repeat but evolve, never exactly identical.",
        "type": "time"
    },
    {
        "id": "phase_transition",
        "description": "Cycles include thresholds where states change dramatically.",
        "type": "time"
    }
]

