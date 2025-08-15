class Particle:
    def __init__(self, name, layer="outer", spin=1):
        self.name = name
        self.energy = 0
        self.matter = 0
        self.layer = layer        # inner / outer
        self.spin = spin          # influences energy distribution
        self.rules = {}           # entity-specific logic rules

    def apply_interaction(self, other):
        # Attraction or repulsion based on layer and energy
        if self.layer == other.layer:
            # similar layers tend to repel slightly if energy high
            if self.energy > 2 and other.energy > 2:
                self.matter -= 0.2
                other.matter -= 0.2
            else:
                self.matter += 0.1
                other.matter += 0.1
        else:
            # inner attracts outer more strongly
            if self.layer == "inner":
                self.matter += 0.3
                other.matter += 0.3
            else:
                self.matter += 0.1
                other.matter += 0.1

