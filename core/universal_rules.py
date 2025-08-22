# core/universal_rules.py
# Version: 2025-08-19 23:15
"""
Universal Basic Logic Rules
---------------------------
This file defines the fundamental logic rules for the pre-ULAI project.
These are not scientific laws but simple universal reasoning seeds.

Layer 1 → Root rules (5)
Layer 2 → Expanded rules (10)
Layer 3 → Interlinked & hidden rules (8)
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
    },

    # --- Layer 3: Interlinked Rules ---
    # Cross-pair rules
    {
        "id": "cascade_balance",
        "description": "Cross-rule: chain_reaction × balance_flow.",
        "type": "hybrid"
    },
    {
        "id": "latent_cycle",
        "description": "Cross-rule: hidden_cause × cycles.",
        "type": "hybrid"
    },
    {
        "id": "stored_connection",
        "description": "Cross-rule: storage_release × interconnection.",
        "type": "hybrid"
    },
    {
        "id": "spiral_feedback",
        "description": "Cross-rule: spiral_growth × feedback_loop.",
        "type": "hybrid"
    },
    {
        "id": "phase_dependency",
        "description": "Cross-rule: phase_transition × mutual_dependence.",
        "type": "hybrid"
    },

    # Hidden / non-detectable rules
    {
        "id": "invisible_equilibrium",
        "description": "Hidden rule: undetectable balance mechanism.",
        "type": "hidden"
    },
    {
        "id": "dark_linkage",
        "description": "Hidden rule: undetectable relation pathway.",
        "type": "hidden"
    },
    {
        "id": "silent_cause",
        "description": "Hidden rule: undetectable cause with observable effects.",
        "type": "hidden"
    },

    # --- Layer 3: Interlinked Rules (continued) ---

    # New rules from cycle/empty/balance reasoning
    {
        "id": "cycle_completion",
        "description": "Cycles include both presence and absence; empty spaces complete the cycle.",
        "type": "completion"
    },
    {
        "id": "waveform_completeness",
        "description": "Waves are completed by their missing crest or trough; absence is part of the form.",
        "type": "completion"
    },
    {
        "id": "balance_between_extremes",
        "description": "Between any two extremes lies a balanced state or range.",
        "type": "balance"
    },

    # --- Candidate rules (proposed but not yet validated) ---
    {
        "id": "waveform_as_workform",
        "description": "A waveform can be seen as the workform of the balance environment between opposites.",
        "type": "candidate"
    },
    {
        "id": "exchange_of_opposites",
        "description": "Energy motion can be understood as an exchange between opposing forces.",
        "type": "candidate"
    },
    {
        "id": "opposite_reaction_strength",
        "description": "The stronger and closer two opposites are, the stronger their reaction.",
        "type": "candidate"
    },
    {
        "id": "group_force_effect",
        "description": "When opposites combine in groups, their collective forces amplify reactions.",
        "type": "candidate"
    }
]

