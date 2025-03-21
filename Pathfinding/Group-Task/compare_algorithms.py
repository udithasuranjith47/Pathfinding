from bfs import bfs
from dfs import dfs

# Run BFS
print("=== Running BFS ===")
bfs_path = bfs()
if bfs_path:
    print("BFS Path Found:", bfs_path)
    print("BFS Path Length (Cost):", len(bfs_path) - 1)
else:
    print("No path found using BFS")

print("\n=============================\n")
# Run DFS
print("=== Running DFS ===")
dfs_path = dfs()
if dfs_path:
    print("DFS Path Found:", dfs_path)
    print("DFS Path Length (Cost):", len(dfs_path) - 1)
else:
    print("No path found using DFS")

print("\n=============================\n")
# Compare Results
if bfs_path and dfs_path:
    bfs_cost = len(bfs_path) - 1
    dfs_cost = len(dfs_path) - 1

    print("=== Comparison of BFS and DFS ===")
    print(f"BFS Path Cost: {bfs_cost}")
    print(f"DFS Path Cost: {dfs_cost}")

    if bfs_cost < dfs_cost:
        print("BFS found the shortest path!")
    elif dfs_cost < bfs_cost:
        print("DFS found a shorter path (not guaranteed).")
    else:
        print("Both algorithms found paths with the same cost.")
elif bfs_path:
    print("Only BFS found a path.")
elif dfs_path:
    print("Only DFS found a path.")
else:
    print("No path found by either algorithm.")
