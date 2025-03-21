
# Defines the 7x7 grid for pathfinding

Grid_Size = 7 # for reason add this Assignment expecting for 7X7 Grid
Start = (0,0) # This is the top left corner is the starting point
End = (6,6) # This is the Bottom-right Corner is the end or goal

# 0 = Open path, 1 = Obstacle (meaning there is walls where movement is blocked) and also this is map of the pathfinding

grid = [
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0]
]

# So now do the function to print the grid

def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))


# below is the run file to check the grid layout is working on not

if __name__ == "__main__":
    print("Grid Layout:")
    print_grid()

    #How to run this file directly "python grid.py" in terminal