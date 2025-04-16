import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Output setup
output_dir = "timespace_sim"
os.makedirs(output_dir, exist_ok=True)
gif_path = os.path.join(output_dir, "cube_to_tesseract.gif")

def generate_tesseract():
    """Returns 4D coordinates of a tesseract (16 vertices)"""
    return np.array([[int(x) for x in f"{i:04b}"] for i in range(16)])

def project_4d_to_3d(points4d, angle=0.0):
    """Rotate and project 4D → 3D"""
    # Rotate in 4D space (between x4 and x1 axes)
    theta = angle
    rotation = np.array([
        [np.cos(theta), 0, 0, -np.sin(theta)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [np.sin(theta), 0, 0, np.cos(theta)]
    ])
    rotated = points4d @ rotation.T

    # Perspective projection: drop 4th dim
    perspective = 1 / (2 - rotated[:, 3])  # Adjust depth
    projected = rotated[:, :3] * perspective[:, np.newaxis]
    return projected

def get_edges(vertices):
    """Return list of edges for cube or tesseract"""
    edges = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if np.sum(np.abs(vertices[i] - vertices[j])) == 1:
                edges.append((i, j))
    return edges

# Initial geometry
tesseract = generate_tesseract()
edges = get_edges(tesseract)

# Animation setup
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.axis('off')

def update(frame):
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')
    ax.set_title("Cube to Tesseract", fontsize=12)

    angle = frame * np.pi / 50
    projected = project_4d_to_3d(tesseract, angle)

    lines = [[projected[start], projected[end]] for start, end in edges]
    line_collection = Line3DCollection(lines, colors='deepskyblue', linewidths=1.5)
    ax.add_collection3d(line_collection)

# Create animation
anim = FuncAnimation(fig, update, frames=100, interval=100)
anim.save(gif_path, writer=PillowWriter(fps=10))
print(f"Saved cube-to-tesseract animation at: {gif_path}")
