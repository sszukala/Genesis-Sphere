import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Time range and epsilon
t = np.linspace(-5, 5, 1000)
epsilon = 0.01

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create initial plot (empty)
line_density, = ax.plot([], [], label='Density ρ(t) = 1 / (t² + ε)', color='crimson')
line_volume, = ax.plot([], [], label='Volume V(t) = t² + ε', color='deepskyblue', linestyle='--')
ax.axvline(0, color='gray', linestyle=':', label='Singularity (t=0)')
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.set_xlabel("Time (t)")
ax.set_ylabel("Value")
ax.set_title("Animated Singularity Model: Big Bang and Big Crunch")
ax.legend()
ax.grid(True)

# Initialize function for the animation
def init():
    line_density.set_data([], [])
    line_volume.set_data([], [])
    return line_density, line_volume

# Update function for the animation
def update(frame):
    # Calculate density and volume
    density = 1 / (t**2 + epsilon)  # Density curve
    volume = t**2 + epsilon  # Volume curve
    
    # Update data based on frame
    line_density.set_data(t[:frame], density[:frame])
    line_volume.set_data(t[:frame], volume[:frame])
    
    return line_density, line_volume

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=30)

# Save the animation
ani.save("singularity_animation.gif", writer="PillowWriter", fps=30)

# Display the animation
plt.show()
