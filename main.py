from universe import Universe
from agents import Particle

if __name__ == "__main__":
    uni = Universe()
    p1 = Particle("SeedParticle")
    uni.add_entity(p1)

    for _ in range(5):
        uni.step()
        print(f"{p1.name} -> Energy: {p1.energy}, Matter: {p1.matter}")

