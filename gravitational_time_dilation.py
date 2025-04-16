import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3e8  # Speed of light (m/s)
M = 1e30  # Mass of the object (kg), example: ~10 solar masses
r = 1e9  # Distance from the object (meters)
t_max = 1e10  # Maximum time for simulation (seconds)
alpha = 1e-9  # Expansion rate constant for the universe (arbitrary for demo)
omega = 0.1  # Projection factor for 4D to 3D (tesseract rotation factor)

# Time Dilation Function (Gravitational)
def gravitational_time_dilation(r, M):
    return np.sqrt(1 - (2 * G * M) / (r * c**2))

# Time-Density Function (Cosmological)
def time_density(t, alpha, omega):
    S_t = 1 / (1 + np.sin(omega * t)**2)  # Projection factor
    D_t = 1 + alpha * t**2  # Dimension expansion factor
    V_shape = 1  # For simplicity, we set volume to 1
    rho_t = V_shape * S_t * D_t  # Space-time density
    return rho_t

# Time Curvature (Inverse of Time-Density)
def time_curvature(rho_t):
    return 1 / rho_t

# Simulating over time
time_values = np.linspace(1, t_max, 1000)
time_densities = [time_density(t, alpha, omega) for t in time_values]
time_curvatures = [time_curvature(rho) for rho in time_densities]

# Gravitational Time Dilation for constant distance (to compare)
gravitational_dilations = [gravitational_time_dilation(r, M) for _ in time_values]

# Plotting the Time-Density and Curvature over Time
plt.figure(figsize=(12, 6))

# Plot Time Density and Curvature
plt.subplot(1, 2, 1)
plt.plot(time_values, time_densities, label='Time Density (ρ(t))')
plt.plot(time_values, time_curvatures, label='Time Curvature (T(t))', linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Density / Curvature')
plt.title('Time Density and Curvature over Time')
plt.legend()

# Plot Gravitational Time Dilation vs Time
plt.subplot(1, 2, 2)
plt.plot(time_values, gravitational_dilations, label='Gravitational Time Dilation', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Time Dilation Factor')
plt.title('Gravitational Time Dilation over Time')
plt.legend()

plt.tight_layout()
plt.show()
