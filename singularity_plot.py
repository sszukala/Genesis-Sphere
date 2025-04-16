import numpy as np
import matplotlib.pyplot as plt
import os

def plot_singularity_density(n=2, t_min=0.01, t_max=10, points=1000, save=True):
    """
    Plots the relationship between density and time near cosmic singularities.
    
    Parameters:
    -----------
    n : float
        Exponent in the density formula ρ(t) = 1/t^n
    t_min : float
        Minimum time value (approaching Big Bang)
    t_max : float
        Maximum time value (approaching Big Crunch, conceptually)
    points : int
        Number of data points to plot
    save : bool
        Whether to save the plot to a file
    
    Returns:
    --------
    None
    """
    # Define time range, avoiding t = 0 to prevent division by zero
    t = np.linspace(t_min, t_max, points)
    
    # Calculate density as a function of time: ρ(t) = 1 / t^n
    rho = 1 / (t ** n)
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Plot the main curve
    plt.plot(t, rho, label=r'$\rho(t) = \frac{1}{t^%d}$' % n, 
             color='crimson', linewidth=2)
    
    # Mark the singularities
    plt.axvline(x=t_min, color='blue', linestyle='--', 
                label=f'Big Bang (t → 0)')
    plt.axvline(x=t_max, color='darkgreen', linestyle='--', 
                label=f'Big Crunch (conceptual)')
    
    # Add shaded region to highlight extreme density near Big Bang
    plt.fill_between(t[t < 0.5], 0, rho[t < 0.5], alpha=0.2, color='blue')
    
    # Configure plot aesthetics
    plt.title("Singularity Behavior: Density vs Time", fontsize=16)
    plt.xlabel("Time (t)", fontsize=12)
    plt.ylabel("Density ρ(t)", fontsize=12)
    plt.ylim(0, np.max(rho) * 1.1)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best')
    plt.tight_layout()
    
    # Save the figure to the project's output directory
    if save:
        output_dir = "timespace_sim"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "singularity_density_plot.png")
        plt.savefig(output_path, dpi=300)
        print(f"Plot saved to: {output_path}")

if __name__ == "__main__":
    # Generate the default plot
    plot_singularity_density()
    
    # Uncomment to generate alternative plots with different parameters
    # plot_singularity_density(n=1, t_min=0.001, t_max=5, 
    #                          save=False)  # Linear density decrease
    
    plt.show()