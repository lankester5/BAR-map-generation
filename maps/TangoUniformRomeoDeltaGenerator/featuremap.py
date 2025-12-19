import random

size = 4097
num_clusters = 30  # number of tree clusters
trees_per_cluster = 5  # trees in each cluster
min_dist_from_start = 200  # avoid start plateaus
min_dist_from_metal = 50  # avoid metal nodes

start_positions = [(500,500),(650,500),(800,900),(3597,3597),(3747,3597),(3847,3297)]
metal_nodes = [(1400,1600),(1800,2000),(2200,2400),(2697,2497),(2897,2747),(3097,2997)]  # simplified mid-valley example

features = []

def too_close(x, z, points, min_dist):
    for px, pz in points:
        if ((x - px)**2 + (z - pz)**2)**0.5 < min_dist:
            return True
    return False

for _ in range(num_clusters):
    cluster_x = random.randint(200, size-200)
    cluster_z = random.randint(200, size-200)
    # avoid starts
    if too_close(cluster_x, cluster_z, start_positions, min_dist_from_start):
        continue
    # avoid metal
    if too_close(cluster_x, cluster_z, metal_nodes, min_dist_from_metal):
        continue
    for _ in range(trees_per_cluster):
        offset_x = cluster_x + random.randint(-30,30)
        offset_z = cluster_z + random.randint(-30,30)
        features.append((offset_x, offset_z))

# Write Lua feature file
with open("feature.lua", "w") as f:
    f.write("return {\n")
    for x, z in features:
        f.write(f"  {{name='tree', x={x}, z={z}}},\n")
    f.write("}\n")

print("Feature placement file saved as 'feature.lua'")
