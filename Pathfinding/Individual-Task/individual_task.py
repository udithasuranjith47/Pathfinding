# individual_task.py - Main execution file for the individual task (A*)

from grid_individual import print_grid
from a_star import a_star
from visualize import visualize_search

# Main execution
if __name__ == "__main__":
    print("=== GRID LAYOUT FOR A* ===")
    print_grid()

    print("\n=== RUNNING A* TO FIND THE PATH ===")
    path, explored_nodes, frames = a_star()

    # Output results
    if path:
        print("\nSUCCESS: Valid path found!")
        print("Path (visited nodes):", path)
        print("Total Cost of the Path:", len(path) - 1)
        print("Explored Nodes:", explored_nodes)
    else:
        print("\nFAILURE: No path found.")

    # Visualize the search process
    print("\n=== VISUALIZING A* SEARCH PROCESS ===")
    visualize_search(frames)