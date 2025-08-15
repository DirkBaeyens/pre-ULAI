from agents import Particle

class Cluster:
    def __init__(self, name):
        self.name = name
        self.entities = []
        self.layer = "outer"
        self.rules = {}

    def add_particle(self, particle):
        self.entities.append(particle)

    def step(self):
        # Apply rules to particles
        for p in self.entities:
            for rule, value in self.rules.items():
                if rule == "energy_boost":
                    p.energy += value
                elif rule == "matter_boost":
                    p.matter += value

        # Interactions between particles
        for i, p1 in enumerate(self.entities):
            for p2 in self.entities[i+1:]:
                p1.apply_interaction(p2)

    def summary(self):
        print(f"Cluster: {self.name}")
        for p in self.entities:
            print(f" - {p.name}, Layer:{p.layer}, Energy:{p.energy:.2f}, Matter:{p.matter:.2f}")


class Planet:
    def __init__(self, name):
        self.name = name
        self.clusters = []
        self.layer = "inner"
        self.rules = {}

    def add_cluster(self, cluster):
        self.clusters.append(cluster)

    def step(self):
        for cluster in self.clusters:
            cluster.step()
            # Planet-level scaling: boost inner clusters more
            if cluster.layer == "inner":
                for p in cluster.entities:
                    p.energy += 0.5

    def summary(self):
        print(f"Planet: {self.name}")
        for cluster in self.clusters:
            cluster.summary()

