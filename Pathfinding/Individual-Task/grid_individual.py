# Grid size and start/end positions
Grid_Size = 7
Start = (0, 0)
End = (6, 6)

# 0 = Open path, 1 = Obstacle (walls)
grid = [
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0]
]

# Function to print the grid
def print_grid():
    print("Grid Layout for Individual Task (A*):")
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Run this file directly to check the grid
if __name__ == "__main__":
    print_grid()