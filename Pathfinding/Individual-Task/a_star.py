import heapq
from grid_individual import Grid_Size, Start, End, grid

# Directions: Right, Down, Left, Up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm
def a_star():
    # Convert grid to list of obstacles
    obstacles = []
    for i in range(Grid_Size):
        for j in range(Grid_Size):
            if grid[i][j] == 1:
                obstacles.append((i, j))

    # Priority queue for A*
    open_list = []
    heapq.heappush(open_list, (0, Start))  # (f-score, node)
    came_from = {}
    g_score = {Start: 0}
    f_score = {Start: heuristic(Start, End)}
    explored_nodes = []  # Track all nodes explored

    # Frames for visualization (grid states at each step)
    frames = []
    grid_display = [[0 for _ in range(Grid_Size)] for _ in range(Grid_Size)]
    for obs in obstacles:
        grid_display[obs[0]][obs[1]] = -1  # Mark obstacles

    while open_list:
        _, current = heapq.heappop(open_list)
        explored_nodes.append(current)  # Track this node

        # Create a frame for visualization
        frame = [[grid_display[i][j] for j in range(Grid_Size)] for i in range(Grid_Size)]
        for node in explored_nodes:
            if node != Start and node != End:
                frame[node[0]][node[1]] = 0.5  # Mark explored nodes
        frame[Start[0]][Start[1]] = 2  # Start position
        frame[End[0]][End[1]] = 3      # End position
        frames.append(frame)

        # Check if we reached the end
        if current == End:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(Start)
            path = path[::-1]  # Reverse the path

            # Final frame with the path
            final_frame = [[grid_display[i][j] for j in range(Grid_Size)] for i in range(Grid_Size)]
            for node in explored_nodes:
                if node != Start and node != End and node not in path:
                    final_frame[node[0]][node[1]] = 0.5  # Explored but not in path
            for p in path:
                if p != Start and p != End:
                    final_frame[p[0]][p[1]] = 1  # Final path
            final_frame[Start[0]][Start[1]] = 2
            final_frame[End[0]][End[1]] = 3
            frames.append(final_frame)

            return path, explored_nodes, frames

        # Explore neighbors
        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < Grid_Size and 0 <= ny < Grid_Size and (nx, ny) not in obstacles:
                new_g_score = g_score[current] + 1

                if (nx, ny) not in g_score or new_g_score < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = new_g_score
                    f_score[(nx, ny)] = new_g_score + heuristic((nx, ny), End)
                    heapq.heappush(open_list, (f_score[(nx, ny)], (nx, ny)))

    return None, explored_nodes, frames  # No path found

# Run this file directly to test A*
if __name__ == "__main__":
    path, explored_nodes, frames = a_star()
    if path:
        print("A* Path Found:", path)
        print("Explored Nodes:", explored_nodes)
    else:
        print("No path found using A*")