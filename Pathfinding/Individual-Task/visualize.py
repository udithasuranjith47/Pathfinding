import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from grid_individual import Grid_Size, Start, End

# Visualize the search process with animation
def visualize_search(frames):
    fig, ax = plt.subplots()

    def update(frame_idx):
        ax.clear()
        # Show the grid with colors
        # -1 = Obstacle (red), 0 = Empty, 0.5 = Explored (light blue), 1 = Path (blue), 2 = Start (green), 3 = End (purple)
        ax.imshow(frames[frame_idx], cmap='coolwarm', vmin=-1, vmax=3)
        ax.set_xticks(range(Grid_Size))
        ax.set_yticks(range(Grid_Size))
        ax.grid(True)
        ax.set_title(f"A* Search Process (Step {frame_idx + 1})")
        return ax,

    # Create animation
    ani = FuncAnimation(fig, update, frames=len(frames), interval=500, repeat=False)
    plt.colorbar(ax.imshow(frames[0], cmap='coolwarm', vmin=-1, vmax=3), ax=ax)
    plt.show()

# Run this file directly to test visualization (with dummy data)
if __name__ == "__main__":
    # Dummy frames for testing
    dummy_frame = [[0 for _ in range(Grid_Size)] for _ in range(Grid_Size)]
    dummy_frame[Start[0]][Start[1]] = 2
    dummy_frame[End[0]][End[1]] = 3
    frames = [dummy_frame] * 5  # 5 identical frames
    visualize_search(frames)