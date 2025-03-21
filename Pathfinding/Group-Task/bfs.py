# bfs.py - Implements Breadth-First Search (BFS) to find the shortest path
from collections import deque
from grid import grid, Start, End, Grid_Size

# Directions: Right, Down, Left, Up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    queue = deque()
    queue.append((Start, [Start]))  # (current position, path taken)

    visited = set()
    visited.add(Start)

    while queue:
        (x, y), path = queue.popleft()

        # If we reached the END, return the path
        if (x, y) == End:
            return path

        # Explore all possible moves
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy  # New coordinates

            if 0 <= nx < Grid_Size and 0 <= ny < Grid_Size and grid[nx][ny] == 0:
                if (nx, ny) not in visited:  # If not visited
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))  # Mark as visited

    return None  # No path found


if __name__ == "__main__":
    path = bfs()
    if path:
        print("Shortest Path Found:", path)
    else:
        print("No path found")
