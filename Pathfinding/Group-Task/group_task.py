from grid import grid, Start, End, Grid_Size, print_grid
from bfs import bfs

# Success Criteria Function
def success_criteria(path):

    if not path:
        return False
    return path[0] == Start and path[-1] == End

# Path Function (accumulates and returns the visited nodes)
def path_function(path):
    return path

# Cost Calculation Function
def cost_calculation(path):
    if not path:
        return float('inf')  # No path found, infinite cost
    return len(path) - 1

# Main execution and output
if __name__ == "__main__":
    print("=== GRID LAYOUT ===")
    print_grid()

    print("\n=== RUNNING BFS TO FIND THE PATH ===")
    path = bfs()  # Get the shortest path using BFS

    # Check Success Criteria
    if success_criteria(path):
        print("\nSUCCESS: Valid path found!")
    else:
        print("\nFAILURE: The path does not meet the success criteria.")

    # Use Path Function to get visited nodes (path)
    visited_path = path_function(path)
    print("Path (visited nodes):", visited_path)

    # Calculate the cost of the path
    total_cost = cost_calculation(visited_path)
    print("Total Cost of the Path:", total_cost)
