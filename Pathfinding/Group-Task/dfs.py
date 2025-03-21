from grid import grid, Start, End, Grid_Size

# Directions: Right, Down, Left, Up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs():
    stack = [(Start, [Start])]  # Stack stores (current position, path taken)
    visited = set()
    visited.add(Start)

    while stack:
        (x, y), path = stack.pop()  # Get the last-added position

        # If we reached the End, return the path
        if (x, y) == End:
            return path

        # Explore all possible moves (right, down, left, up)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy  # New coordinates

            if 0 <= nx < Grid_Size and 0 <= ny < Grid_Size and grid[nx][ny] == 0:
                if (nx, ny) not in visited:  # If not visited
                    stack.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))  # Mark as visited

    return None  # No path found

if __name__ == "__main__":
    path = dfs()
    if path:
        print("DFS Path Found:", path)
    else:
        print("No path found using DFS")
