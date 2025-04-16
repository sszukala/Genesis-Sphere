import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Create output directory
output_dir = "timespace_sim"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "singularity_animation.gif")

# Time range and epsilon (reduced number of points for better performance)
t = np.linspace(-5, 5, 200)  # Reduced from 1000 to 200 points
epsilon = 0.01

# Pre-calculate data
density = 1 / (t**2 + epsilon)  # Density curve
volume = t**2 + epsilon  # Volume curve

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create initial plot
line_density, = ax.plot([], [], label='Density ρ(t) = 1 / (t² + ε)', color='crimson', linewidth=2)
line_volume, = ax.plot([], [], label='Volume V(t) = t² + ε', color='deepskyblue', linestyle='--', linewidth=2)
ax.axvline(0, color='gray', linestyle=':', label='Singularity (t=0)')

# Set up plot aesthetics
ax.set_xlim(-5, 5)
ax.set_ylim(0, min(10, np.max(density) * 1.1))  # Dynamic y limit
ax.set_xlabel("Time (t)", fontsize=12)
ax.set_ylabel("Value", fontsize=12)
ax.set_title("Universe Evolution: Density and Volume Near Singularity", fontsize=14)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Initialize function
def init():
    line_density.set_data([], [])
    line_volume.set_data([], [])
    return line_density, line_volume

# Update function (simplified to improve performance)
def update(frame):
    # Use frame to determine how much of the data to show (starting from the middle)
    mid = len(t) // 2
    start = max(0, mid - frame)
    end = min(len(t), mid + frame)
    
    # Update both lines at once
    line_density.set_data(t[start:end], density[start:end])
    line_volume.set_data(t[start:end], volume[start:end])
    
    return line_density, line_volume

# Create animation with fewer frames
frames = 100  # Reduced number of frames
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Save animation with explicit PillowWriter
try:
    print(f"Saving animation to {output_path}...")
    writer = PillowWriter(fps=15)  # Reduced fps for smaller file
    ani.save(output_path, writer=writer)
    print(f"Animation saved successfully!")
except Exception as e:
    print(f"Error saving animation: {e}")

# Show the plot
plt.tight_layout()
plt.show()
