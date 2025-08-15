# Entities that follow universal logic
class Particle:
    def __init__(self, name, layer="outer", spin=1):
        self.name = name
        self.energy = 0
        self.matter = 0
        self.layer = layer        # inner / outer
        self.spin = spin          # influences energy distribution

    def __repr__(self):
        return f"{self.name} (Layer:{self.layer}, Spin:{self.spin}) E:{self.energy}, M:{self.matter}"

