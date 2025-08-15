from universe import Universe
from agents import Particle
from structures import Cluster, Planet

if __name__ == "__main__":
    uni = Universe()

    # --- Create nested structure ---
    p_inner = Particle("CoreSeed", layer="inner", spin=2)
    p_outer1 = Particle("OuterCloud1", layer="outer", spin=1)
    p_outer2 = Particle("OuterCloud2", layer="outer", spin=1)

    cluster1 = Cluster("ClusterAlpha")
    cluster1.add_particle(p_outer1)
    cluster1.add_particle(p_outer2)
    cluster1.rules["energy_boost"] = 0.2

    planet1 = Planet("PlanetX")
    planet1.add_cluster(cluster1)

    uni.add_entity(p_inner)  # inner particle outside the cluster
    uni.add_entity(planet1)  # nested structure

    # --- Run steps ---
    for i in range(5):
        print(f"--- Step {i+1} ---")
        uni.step()
        uni.summary()
        planet1.step()
        planet1.summary()

