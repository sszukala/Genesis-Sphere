import numpy as np
import matplotlib.pyplot as plt

# Define time range, avoiding t = 0 to prevent division by zero
t = np.linspace(0.01, 10, 1000)

# Define density as a function of time: ρ(t) = 1 / t^n
# You can change n to see how fast density grows
n = 2
rho = 1 / (t ** n)

# Plot setup
plt.figure(figsize=(10, 6))
plt.plot(t, rho, label=r'$\rho(t) = \frac{1}{t^%d}$' % n, color='crimson', linewidth=2)

# Mark Big Bang (t → 0) and Big Crunch (t → ∞ conceptually)
plt.axvline(x=0.01, color='gray', linestyle='--', label='Big Bang → t → 0')
plt.axvline(x=10, color='gray', linestyle='--', label='Big Crunch → t → ∞')

# Labels and title
plt.title("Singularity Behavior: Density vs Time", fontsize=16)
plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("Density ρ(t)", fontsize=12)
plt.ylim(0, np.max(rho) * 1.1)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig("singularity_density_plot.png", dpi=300)
plt.show()
