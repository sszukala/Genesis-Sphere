import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Set up output directory and file path
output_dir = "timespace_sim"
os.makedirs(output_dir, exist_ok=True)
save_path = os.path.join(output_dir, "cube_sphere_emergent_space.gif")

# 3D cube (unit cube centered at origin)
cube_vertices = np.array([[x, y, z]
                          for x in (-1, 1)
                          for y in (-1, 1)
                          for z in (-1, 1)])

cube_edges = [(i, j) for i in range(len(cube_vertices))
              for j in range(i+1, len(cube_vertices))
              if np.sum(np.abs(cube_vertices[i] - cube_vertices[j])) == 2]

# Generate tesseract (4D cube)
def generate_tesseract():
    return np.array([[int(x) for x in f"{i:04b}"] for i in range(16)])

# Project 4D to 3D
def project_4d(points4d, theta):
    rot = np.array([
        [np.cos(theta), 0, 0, -np.sin(theta)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [np.sin(theta), 0, 0, np.cos(theta)]
    ])
    rotated = points4d @ rot.T
    perspective = 1 / (2 - rotated[:, 3])
    projected = rotated[:, :3] * perspective[:, None]
    return projected

# 4D tesseract setup
tesseract4d = generate_tesseract()
tesseract_edges = [(i, j) for i in range(len(tesseract4d))
                   for j in range(i+1, len(tesseract4d))
                   if np.sum(np.abs(tesseract4d[i] - tesseract4d[j])) == 1]

# Animation
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.axis('off')

def update(frame):
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.axis('off')

    # Define sphere grid variables (moved outside conditional blocks)
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    x = np.sqrt(3) * np.cos(u) * np.sin(v)
    y = np.sqrt(3) * np.sin(u) * np.sin(v)
    z = np.sqrt(3) * np.cos(v)

    # PHASE 2: Draw cube
    if frame < 30:
        lines = [[cube_vertices[i], cube_vertices[j]] for i, j in cube_edges]
        ax.add_collection3d(Line3DCollection(lines, colors='deepskyblue', linewidths=2))

        # Overlay sphere touching cube corners
        ax.plot_surface(x, y, z, color='gray', alpha=0.1, linewidth=0)

    # PHASE 3: Emergent space + collapse
    else:
        alpha = max(0, 1 - (frame - 30)/40)
        theta = (frame - 30) * np.pi / 50
        projected = project_4d(tesseract4d, theta)
        lines = [[projected[i], projected[j]] for i, j in tesseract_edges]
        ax.add_collection3d(Line3DCollection(lines, colors=(1, 0.3, 0.3, alpha), linewidths=1.5))

        # Optional: decay sphere effect
        r = np.sqrt(3)
        ax.plot_wireframe(r * x, r * y, r * z, color='gray', alpha=0.05 + 0.2*alpha, linewidth=0.2)

# Generate animation
ani = FuncAnimation(fig, update, frames=80, interval=80)
writer = PillowWriter(fps=10)
ani.save(save_path, writer=writer)
print(f"GIF saved to: {save_path}")
