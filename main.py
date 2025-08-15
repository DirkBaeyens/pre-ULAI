from universe import Universe
from agents import Particle

if __name__ == "__main__":
    uni = Universe()
    
    # Add inner and outer entities
    p1 = Particle("CoreSeed", layer="inner", spin=2)
    p2 = Particle("OuterCloud", layer="outer", spin=1)
    p3 = Particle("OuterCloud2", layer="outer", spin=1)
    
    # Assign entity-specific rules
    p1.rules["energy_boost"] = 1
    p2.rules["matter_boost"] = 0.5

    uni.add_entity(p1)
    uni.add_entity(p2)
    uni.add_entity(p3)

    for i in range(5):
        print(f"--- Step {i+1} ---")
        uni.step()
        uni.summary()

