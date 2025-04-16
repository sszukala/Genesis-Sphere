import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation, PillowWriter

# Output settings
output_dir = "timespace_sim"
os.makedirs(output_dir, exist_ok=True)
gif_path = os.path.join(output_dir, "emergent_space.gif")

# Define cube vertices and faces
cube_vertices = np.array([
    [0, 0, 0], [1, 0, 0],
    [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1],
    [1, 1, 1], [0, 1, 1]
])

cube_faces = [
    [0, 1, 2, 3], [4, 5, 6, 7],
    [0, 1, 5, 4], [2, 3, 7, 6],
    [1, 2, 6, 5], [3, 0, 4, 7]
]

# Function to draw a cube
def draw_cube(ax, vertices, faces, alpha=0.4, color='cyan'):
    for face in faces:
        square = [vertices[i] for i in face]
        poly3d = Poly3DCollection([square], alpha=alpha, facecolors=color, edgecolor='k')
        ax.add_collection3d(poly3d)

# Animation frame update function
def update(frame):
    ax.clear()
    ax.set_title(f"Time Step {frame}", fontsize=12)
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.5)
    ax.set_zlim(0, 1.5)
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')

    if frame == 0:
        pass  # Void
    elif frame == 1:
        ax.scatter([0.5], [0.5], [0.5], color='black')  # Point
    elif frame == 2:
        ax.plot([0.5, 1], [0.5, 0.5], [0.5, 0.5], color='black')  # Line
    elif frame == 3:
        ax.plot_trisurf(
            [0.5, 1, 1],
            [0.5, 0.5, 1],
            [0.5, 0.5, 0.5],
            color='gray', alpha=0.6
        )  # Triangle
    elif frame == 4:
        tetra = [[0.5, 0.5, 0.5], [1, 0.5, 0.5], [1, 1, 0.5], [0.75, 0.75, 1]]
        tetra_faces = [
            [tetra[0], tetra[1], tetra[2]],
            [tetra[0], tetra[1], tetra[3]],
            [tetra[1], tetra[2], tetra[3]],
            [tetra[2], tetra[0], tetra[3]]
        ]
        for face in tetra_faces:
            poly3d = Poly3DCollection([face], alpha=0.6, facecolors='lightblue', edgecolor='k')
            ax.add_collection3d(poly3d)
    else:
        draw_cube(ax, cube_vertices, cube_faces)

# Build the animation
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
anim = FuncAnimation(fig, update, frames=6, interval=1000)

# Save to GIF
anim.save(gif_path, writer=PillowWriter(fps=1))
print(f"GIF saved to: {gif_path}")
