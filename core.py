# Core universal logic rules
class UniversalLogic:
    def __init__(self):
        self.rules = {
            "energy_flow": "core_outward",
            "matter_inflow": "external_inward",
            "cycle": "overload_dispersal_inflow",
            "structure": "disk_inner_bulb_outer",
            "spin_effect": "affects_distribution",
            "transparency": "entities_interact_without_barriers",
            "hot_fire_cold_fuel": "energy_gradient_replenishment"
        }

    def apply_rules(self, obj):
        # Energy flows outward, matter flows inward
        obj.energy += 1 * obj.spin
        obj.matter += 0.5  # slow inflow
        # Outer layers accumulate more matter, inner layers more energy
        if obj.layer == "inner":
            obj.energy += 1
        else:
            obj.matter += 1
        return obj

