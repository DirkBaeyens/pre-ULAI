from universe import Universe
from agents import Particle

if __name__ == "__main__":
    uni = Universe()
    
    # Add inner and outer entities
    p1 = Particle("CoreSeed", layer="inner", spin=2)
    p2 = Particle("OuterCloud", layer="outer", spin=1)
    
    uni.add_entity(p1)
    uni.add_entity(p2)

    for i in range(5):
        print(f"--- Step {i+1} ---")
        uni.step()
        uni.summary()

