import numpy as np
import matplotlib.pyplot as plt
import os

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3e8  # Speed of light (m/s)
M = 1e30  # Mass of the object (kg), example: ~10 solar masses
r = 1e9  # Distance from the object (meters)
t_max = 1e10  # Maximum time for simulation (seconds)
alpha = 1e-9  # Expansion rate constant for the universe (arbitrary for demo)
omega = 0.1  # Projection factor for 4D to 3D (tesseract rotation factor)
beta = 1e9  # Temporal drag coefficient
epsilon = 1e5  # Small constant to avoid division by zero

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

# Temporal Flow Ratio
def temporal_flow_ratio(t, beta, epsilon):
    return 1 / (1 + beta / (np.abs(t) + epsilon))

# Effective Time (Curvature * Flow Ratio)
def effective_time(t, alpha, omega, beta, epsilon):
    curvature = time_curvature(time_density(t, alpha, omega))
    flow_ratio = temporal_flow_ratio(t, beta, epsilon)
    return curvature * flow_ratio

# Perceived Time (Integration of Flow Ratio)
def perceived_time(t_values, beta, epsilon):
    flow_ratios = [temporal_flow_ratio(t, beta, epsilon) for t in t_values]
    # Numerical integration using trapezoidal rule
    dt = t_values[1] - t_values[0]
    perceived = np.zeros_like(t_values)
    for i in range(1, len(t_values)):
        perceived[i] = perceived[i-1] + 0.5 * dt * (flow_ratios[i-1] + flow_ratios[i])
    return perceived

# Simulating over time
time_values = np.linspace(1, t_max, 1000)
time_densities = [time_density(t, alpha, omega) for t in time_values]
time_curvatures = [time_curvature(rho) for rho in time_densities]

# Calculate new metrics
flow_ratios = [temporal_flow_ratio(t, beta, epsilon) for t in time_values]
effective_times = [effective_time(t, alpha, omega, beta, epsilon) for t in time_values]
perceived_times = perceived_time(time_values, beta, epsilon)

# Gravitational Time Dilation for constant distance (to compare)
gravitational_dilations = [gravitational_time_dilation(r, M) for _ in time_values]

# Create output directory if it doesn't exist
output_dir = "timespace_sim"
os.makedirs(output_dir, exist_ok=True)

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
plt.savefig(os.path.join(output_dir, 'time_density_dilation.png'), dpi=300)

# New plot for Temporal Flow concepts
plt.figure(figsize=(15, 5))

# Plot Temporal Flow Ratio
plt.subplot(1, 3, 1)
plt.plot(time_values, flow_ratios, label='R(t)', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Flow Ratio')
plt.title('Temporal Flow Ratio')
plt.legend()

# Plot Effective Time
plt.subplot(1, 3, 2)
plt.plot(time_values, effective_times, label='Tₑffₑctᵢᵥₑ(t)', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Effective Time')
plt.title('Effective Time (Curvature * Flow)')
plt.legend()

# Plot Perceived Time
plt.subplot(1, 3, 3)
plt.plot(time_values, perceived_times, label='Tₚₑᵣcₑᵢᵥₑd(t)', color='blue')
plt.plot(time_values, time_values, label='Linear Time', color='gray', linestyle='--')
plt.xlabel('Observer Time (s)')
plt.ylabel('Perceived Time')
plt.title('Perceived vs Linear Time')
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'temporal_flow_concepts.png'), dpi=300)

plt.show()
