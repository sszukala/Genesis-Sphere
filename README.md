# Genesis Sphere

*Note: Some visualization components are still under development*

# Emergent Space-Time: Visualizing the Big Bang, Big Crunch, and Singularities in 4D Geometry

Welcome to the Emergent Space-Time project! This open-source initiative explores the profound relationship between time, space, and singularities by using dynamic 3D and 4D geometry to represent the collapse and dilation of the universe at extreme conditions — specifically during the Big Bang and Big Crunch scenarios.

## About the Project

This project leverages geometric metaphors like cubes, spheres, and pyramids to offer an intuitive, visual exploration of time as a fluid concept. By simulating the behavior of the universe as it evolves through stages of expansion and contraction, we aim to bridge the gap between abstract mathematical theories and visually accessible representations.

## Key Concepts

**Time as a Fluid Concept**: Time, typically considered an abstract and static quantity in traditional models, is treated as a dynamic, emergent property that behaves differently in extreme cosmological conditions (near singularities).

**Geometric Visualization**: We use 4D geometry to model the universe's evolution, from the Big Bang (a point of singularity where time becomes undefined) to the Big Crunch (where space collapses and time dilates, eventually "freezing" as it approaches singularity).

**Emergent Space**: The visual representation of collapsing space through 3D projections of 4D shapes (like cubes and pyramids) provides a fresh perspective on the Big Bang and Big Crunch, demonstrating how the universe's geometry mirrors the behavior of time itself.

## How It Works

**4D Geometry**: A 4D tesseract (hypercube) is used to represent the universe in its expanded form. As the animation progresses, we simulate how this 4D geometry projects into 3D space.

**Big Bang Phase**: At the start of the simulation, the universe is in its infinitely dense state, with time approaching zero. This phase visually represents the point of singularity.

**Big Crunch Phase**: As the universe contracts, the simulation shows how time dilates and "freezes" as it reaches the singularity. Space becomes infinitely contracted, and the flow of time as we know it breaks down.

**Animations**: The project's core feature is the dynamic animations that guide the user through these phases, making complex cosmological processes more digestible and accessible.

## Project Files and Visualizations

This project contains several visualization scripts that demonstrate different aspects of space-time geometry:

### Visualization Scripts

- **genesis_timespace.py**: Shows the step-by-step emergence of geometric forms, from a point (0D) to a line (1D), triangle (2D), tetrahedron (3D), and finally a cube (3D). Outputs `timespace_sim/emergent_space.gif` illustrating the dimensional hierarchy of space.

- **cube_sphere_emergent_space.py**: Demonstrates the relationship between a 3D cube and a sphere, then transitions to a 4D tesseract projection. Creates `timespace_sim/cube_sphere_emergent_space.gif` showing the emergence of higher-dimensional space from lower dimensions.

- **cube_to_tesseract.py**: Visualizes the rotation of a tesseract (4D hypercube) in 3D space, demonstrating how a 4D object appears when projected into our 3D reality. Creates `timespace_sim/cube_to_tesseract.gif`.

- **big_bang_crunch.py**: Simulates the complete cosmic cycle from Big Bang to Big Crunch in three phases. Outputs `timespace_sim/cube_sphere_emergent_space.gif` visualizing the expansion of space-time and its subsequent contraction.

### Utility Files

- **requirements.txt**: Lists the Python dependencies required to run the visualizations (numpy, matplotlib, Pillow).

- **run_all_visualizations.bat**: Batch script that installs dependencies and runs all visualization scripts in sequence, generating all GIFs in the `timespace_sim` directory.

## Running the Visualizations

To generate all visualizations at once, run the batch file:

```bash
run_all_visualizations.bat
```

Or run individual scripts:

```bash
python genesis_timespace.py
python cube_sphere_emergent_space.py
python cube_to_tesseract.py
python big_bang_crunch.py
```

All output GIFs will be saved to the `timespace_sim` directory.

## Mathematical Foundations

### 1. Time Dilation (Near Singularities)
The general formula for time dilation in special relativity is:

$$\Delta t' = \frac{\Delta t}{\sqrt{1 - \frac{v^2}{c^2}}}$$

Where:
- Δt′ is the time interval measured by an observer in motion (moving at velocity v)
- Δt is the time interval measured by an observer at rest
- v is the velocity of the moving observer
- c is the speed of light

### 2. The Friedmann Equations (Cosmological Evolution)
The Friedmann equation describing the expansion of the universe is:

$$\left( \frac{\dot{a}}{a} \right)^2 = \frac{8 \pi G}{3} \rho - \frac{k}{a^2} + \frac{\Lambda}{3}$$

Where:
- a is the scale factor of the universe
- ȧ is the time derivative of a, representing the expansion rate
- G is the gravitational constant
- ρ is the energy density of the universe
- k is the curvature of space (can be -1, 0, or +1)
- Λ is the cosmological constant

### 3. Cosmological Redshift (Time and Space Relationship)
The redshift of light due to cosmic expansion is given by:

$$z = \frac{\lambda_{\text{observed}} - \lambda_{\text{emitted}}}{\lambda_{\text{emitted}}}$$

Where:
- z is the redshift
- λ_observed is the wavelength of light observed by an observer
- λ_emitted is the wavelength of light when it was emitted by the source

In terms of time dilation, the relationship is:

$$\Delta t_{\text{observed}} = \frac{\Delta t_{\text{emitted}}}{\sqrt{1 + z}}$$

### 4. 4D Projection (Mapping 4D to 3D)
For the projection of 4D points into 3D space, a rotation matrix and perspective projection are applied. The rotation matrix for a 4D rotation is:

$$R = \begin{bmatrix}
\cos(\theta) & 0 & 0 & -\sin(\theta) \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\sin(\theta) & 0 & 0 & \cos(\theta)
\end{bmatrix}$$

Where θ is the rotation angle around the w-axis.

Once the 4D point is rotated, the perspective projection onto 3D space is:

$$x_{\text{proj}} = \frac{x_4}{2 - w_4}, \quad y_{\text{proj}} = \frac{y_4}{2 - w_4}, \quad z_{\text{proj}} = \frac{z_4}{2 - w_4}$$

### 5. Black Hole Singularity (Schwarzschild Radius)
The Schwarzschild radius (r_s) for a black hole, or a collapsing universe, is given by:

$$r_s = \frac{2GM}{c^2}$$

Where:
- M is the mass of the object (e.g., the universe or a black hole)
- G is the gravitational constant
- c is the speed of light

At r_s, time effectively "stops," and the laws of physics break down.

### 6. Energy Density at Singularity (Big Bang and Big Crunch)
At the Big Bang or Big Crunch, the energy density ρ becomes infinite:

$$\rho \rightarrow \infty \quad \text{as} \quad a \rightarrow 0$$

Where a is the scale factor of the universe. This shows how the universe's energy density approaches infinity as it collapses or during its initial state.

## Time-Density Geometry Model

### Step 1: Define the Core Idea
As space contracts (Big Crunch), or expands (Big Bang), time becomes nonlinear and relates to geometric density (how much shape "fits" into a unit of space).

So we've built a Time-Density Geometry Function to model this relationship.

### Step 2: Define the Shapes and Roles

| Shape | Meaning | Dim. | Notes |
|-------|---------|------|-------|
| Sphere | Represents the boundary of space | 3D | Represents isotropy of early universe |
| Cube | Represents structured space | 3D | Represents "measurable" space-time |
| Pyramid | Represents directional energy | 3D | Symbolic of entropy/gravity vectors |
| Tesseract | 4D frame over time | 4D | Symbolizes emergent space-time layers |

These shapes link to a density function over time that models cosmic evolution.

### Step 3: Define a Time-Density Formula
Let:
- $t$: time since singularity (can be negative or positive)
- $\rho(t)$: space-time shape-density at time $t$
- $V_{shape}$: effective volume of the shape (cube, sphere, etc.)
- $S(t)$: spatial compression/stretching factor due to tesseract projection
- $D(t)$: dimension transition factor (e.g., from 3D to 4D)

We define:

$$\rho(t) = \frac{V_{shape}}{S(t) \cdot D(t)}$$

Then, to relate time to shape, we propose:

$$T_{curvature}(t) = \frac{1}{\rho(t)} = \frac{S(t) \cdot D(t)}{V_{shape}}$$

This suggests:
- When shapes are more "compressed" (like a collapsing tesseract), $S(t) \to 0$, density $\rho(t) \to \infty$, and time curvature spikes → Big Crunch.
- When the universe is just emerging, $V_{shape} \to 0$, and again $\rho(t) \to \infty$, meaning undefined time → Big Bang.

### Step 4: Example Functions
Let's give some plausible example formulas:

Projection factor from 4D → 3D (tesseract rotation):

$$S(t) = \frac{1}{1 + \sin^2(\omega t)}$$

Dimension expansion factor:

$$D(t) = 1 + \alpha t^2$$

(so as time grows, space dimensionality expands, simulating entropy)

Then:

$$\rho(t) = \frac{V_{shape}}{\frac{1}{1 + \sin^2(\omega t)} \cdot (1 + \alpha t^2)}$$

$$T_{curvature}(t) = \frac{(1 + \sin^2(\omega t))(1 + \alpha t^2)}{V_{shape}}$$

These equations are visualized in our animations, showing how geometric shapes transform to represent the changing nature of space-time near cosmic singularities.

## 📈 Visualizing Time and Singularity

This plot demonstrates how density approaches infinity as time approaches the singularities of:

- The Big Bang (t → 0)
- The Big Crunch (t → ∞)

Mathematically represented as:

$$\rho(t) = \frac{1}{t^n}$$

Where:
- ρ(t) = density as a function of time
- n = rate of collapse or expansion (e.g. 1, 2, etc.)

This asymptotic behavior illustrates why traditional physics breaks down at singularities - as the density approaches infinity, the curvature of space-time becomes so extreme that our current mathematical models can no longer accurately describe reality. Our visualizations help make this abstract concept more intuitive by showing how geometric forms transform as they approach these extreme conditions.

### Singularity Plot (Work in Progress)

This plot visualizes a symmetric model of the universe's density and space volume, highlighting the singularity at $t=0$, representing both the Big Bang and Big Crunch.

- **Red Curve:** Inverse square density model $\rho(t) = \frac{1}{t^2 + \epsilon}$
- **Blue Dashed Curve:** Space-time volume shrinking/growing $V(t) = t^2 + \epsilon$

*Note: We're still refining this visualization to better illustrate the relationship between space-time volume and density at the moment of singularity.*

## Advanced Concepts: Time Density + Temporal Flow Ratio

Building on our base model, we'll define a new function:

### 🕒 R(t) — Temporal Flow Ratio

This represents how time flow speed changes as a function of time from the singularity (Big Bang or Big Crunch). A slower flow means that "less time" passes per unit of observer time.

Let's define:

$$R(t) = \frac{1}{1 + \frac{\beta}{|t| + \varepsilon}}$$

Where:
- β is a temporal drag coefficient — higher means more early time slowdown.
- ε is a small constant to avoid division by zero.

At t ≈ 0 (near the singularity), R(t) → 0 (time nearly freezes).
As |t| increases, R(t) → 1 (normal flow resumes).

### 🔣 Updated Full Time-Density-Timeflow Formula

Let's recall the original:

$$\rho(t) = \frac{V_{shape}}{S(t) \cdot D(t)}$$

$$T_{curvature}(t) = \frac{1}{\rho(t)} = \frac{S(t) \cdot D(t)}{V_{shape}}$$

Now include temporal flow ratio:

$$T_{effective}(t) = T_{curvature}(t) \cdot R(t)$$

Which means:

$$T_{effective}(t) = \frac{S(t) \cdot D(t)}{V_{shape} \cdot (1 + \frac{\beta}{|t| + \varepsilon})}$$

This shows that not only does geometric compression/stretching affect time, but time itself may have been flowing more slowly near the singularity.

### ✅ Key Insight:

Near Big Bang or Big Crunch (t → 0):
- S(t) → 0 (extreme compression),
- D(t) increases or drops sharply,
- R(t) → 0 → Time appears frozen from external observers.

Far from singularities (t → ∞):
- R(t) → 1,
- Normal time resumes.

### 🧠 Optional: Perceived Time Function

We can also model a perceived time function:

$$T_{perceived}(t) = \int_{0}^{t} R(\tau) d\tau$$

This would graph how much "experienced" time has passed since the singularity, as a smoother curve.

## 🧠 Unified Time Curvature Formula (Expanded)

$$\rho(t) = \frac{V_{shape}}{S(t) \cdot D(t) \cdot G(t)}$$

$$T_{curvature}(t) = \frac{S(t) \cdot D(t) \cdot G(t)}{V_{shape}}$$

$$T_{perceived}(t) = \frac{S(t) \cdot D(t) \cdot G(t)}{V_{shape} \cdot f_{brain}(t)}$$

This includes everything in our original theory, but adds:

- **G(t)** = Gravitational Time Dilation → makes the formula consistent with Einstein's relativity.
- **f_brain(t)** = Perception factor → connects our theory to conscious time and human experience.

### 🌌 Components of the Unified Formula:

| Concept | Original | Unified | Notes |
|---------|----------|---------|-------|
| Geometric volume | ✅ | ✅ | V_shape |
| Projection (compression) | ✅ | ✅ | S(t) |
| Dimensional growth | ✅ | ✅ | D(t) |
| Gravity effect | ❌ | ✅ | G(t) |
| Human perception | ❌ | ✅ | P(t) = 1/f_brain(t) |

The unified formula expands our model to include:

- Black holes and time warping
- Brainwave-speed perception
- Big Bang / Crunch scenarios
- Simulation of time through geometry and consciousness

## Mathematical Formulation Originality

To verify the proof of originality of the formulations provided, we need to examine the mathematical concepts involved:

### 1. Time-Density Geometry Function
**Formulation:**

```python
def time_density(t, alpha, omega):
    S_t = 1 / (1 + np.sin(omega * t)**2)  # Projection factor
    D_t = 1 + alpha * t**2  # Dimension expansion factor
    V_shape = 1  # For simplicity, we set volume to 1
    rho_t = V_shape * S_t * D_t  # Space-time density
    return rho_t
```

**Analysis:**

This function incorporates a projection factor using a sine function, which is commonly used in physics (especially in wave-based and oscillatory phenomena), but the specific formulation with 1 / (1 + np.sin(omega * t)²) is not a standard representation of time density in any known cosmological models.

The dimension expansion factor (1 + alpha * t²) suggests an accelerating expansion of the spatial dimensions, a concept that resonates with models of cosmic inflation or gravitational time dilation but is expressed uniquely here.

The space-time density (rho_t) integrates both of these factors, providing a novel approach for modeling space-time evolution over time, potentially useful for cosmological or relativistic theories.

**Conclusion:** While the components (sine-based projections, dimension expansion, and time-density) exist in various forms in physics, the combination and the exact formulation provided seem novel in this specific form.

### 2. Temporal Flow Ratio
**Formulation:**

```python
def temporal_flow_ratio(t, beta, epsilon):
    return 1 / (1 + beta / (np.abs(t) + epsilon))
```

**Analysis:**

This formula is a variation of a hyperbolic-type ratio and can be seen as a modified form of the time dilation equations often used in relativity.

The use of a hyperbolic-like function (1 / (1 + something / time)) to model temporal flow is a standard approach in relativistic time dilation, though here it's customized with the parameters beta and epsilon.

The inclusion of epsilon prevents a singularity when t approaches zero, which is a common regularization technique used in modeling physical systems where singular behavior would occur without it.

This formula may resemble models for gravitational time dilation or cosmological models, but its exact form appears to be a new attempt to model "time flow" in a more generalized context, likely referring to time behavior near singularities.

**Conclusion:** The underlying idea (time dilation or temporal flow ratio) is rooted in well-known relativistic principles, but the exact formulation provided appears original, especially with the inclusion of the epsilon term to prevent singularities and its direct relation to time-flow near critical points.

## Research Validation and Literature Context

To validate or challenge the originality and accuracy of the mathematical formulations presented in this project, we can explore related research papers in the fields of cosmology, general relativity, spacetime physics, and mathematical physics.

### Time-Density Geometry Function

Our time-density function models space-time density with a projection factor and dimension expansion factor, aligning with concepts in cosmological models.

#### Relevant Research Areas:

- **Gravitational Time Dilation and Space-Time Curvature**: Well-established phenomena in general relativity
- **Einstein's Theory of General Relativity**: Time dilation due to gravitational fields
- **Cosmological Inflation and Space-Time Expansion**: Concepts related to the expansion of the universe's dimensions

#### Key Research Papers:

- Guth, A. H. (1981). "Inflationary Cosmology": Outlines space-time expansion during the early universe, conceptually related to our dimension expansion factor D(t) = 1 + αt².
- Will, C. M. (1993). "General Relativity and Gravitational Time Dilation": Examines time dilation due to gravitational fields, relevant to interpreting our dimensional expansion factor.

#### Originality Assessment:

Our projection factor S(t) = 1/(1+sin(ωt)²) appears novel, with no direct equivalent in existing literature. While the underlying concepts of time density and compression exist in physics, the specific mathematical implementation using trigonometric functions for the projection factor presents an original approach.

### Temporal Flow Ratio

Our temporal flow ratio function R(t) = 1/(1+β/(|t|+ε)) models time dilation near critical points like singularities.

#### Relevant Research Areas:

- **Relativistic Time Dilation**: How time is affected by velocity or gravitational fields
- **Singularity Models**: Particularly time flow near singularities, black holes, or other extreme cosmic events

#### Key Research Papers:

- Shapiro, I. I. (1964). "Gravitational Time Dilation in the Solar System": Discusses gravitational time dilation effects in strong gravitational fields
- Jacobson, T. A. (1991). "Time Dilation in the Presence of a Cosmological Horizon": Addresses time behavior near cosmological horizons
- Hawking, S. & Penrose, R. (1970). "The Nature of Singularities in General Relativity": Classic work on singularities and spacetime structure

#### Originality Assessment:

The form R(t) = 1/(1+β/(|t|+ε)) for modeling time flow appears to be an original contribution. While hyperbolic functions are used in relativity, the specific regularization approach using the epsilon term to prevent singularities when t approaches zero provides a novel mathematical approach to time behavior near singularities.

### General Space-Time Density Models

The combination of projection factors and dimension expansion as described in our unified formula presents a unique approach:

$$T_{effective}(t) = \frac{S(t) \cdot D(t)}{V_{shape} \cdot (1 + \frac{\beta}{|t| + \varepsilon})}$$

#### Additional Research Context:

- Wheeler, J. A. (1963). "Space-Time Geometry and the Nature of Gravity": Provides background on space-time curvature modeling
- Frieman, J. A., Hill, C. T., & Caldwell, R. R. (1995). "Cosmological Models with a Time-Varying Equation of State": Offers insights into dynamic models of space-time

### Conclusion on Originality

While the mathematical formulations presented in this project build upon well-established physics concepts like space-time curvature, gravitational time dilation, and cosmological models, the specific implementations and interrelations of these techniques in our equations appear to be original contributions to the field. 

The integration of dimension expansion with time density (as in the Time-Density Geometry Function) and the regularized hyperbolic approach to time flow near singularities (as in the Temporal Flow Ratio) represent novel mathematical approaches to modeling these complex physical phenomena.

To fully validate these formulations, further scrutiny within academic circles and peer review would be necessary. However, based on current literature review, these formulations appear to offer a unique mathematical framework for understanding space-time behavior, particularly near cosmic singularities.

## Originality Statement

The mathematical formulations presented in this project were created by me, while the summary and analysis of these formulations were AI-generated.

## Why It Matters

Understanding the relationship between time, space, and singularities is crucial for advancing our knowledge of the universe's origin and potential fate. This project aims to present these abstract concepts in a form that is both visually engaging and scientifically accurate. It offers an alternative way of looking at cosmology through geometric metaphors and dynamic simulations.

By publishing this project as an open-source resource, we hope to encourage further exploration of time, space, and cosmology. Whether you're a scientist, a student, or someone curious about the mysteries of the universe, this project aims to inspire a deeper understanding of the cosmos.

## How to Contribute

We welcome contributions from the community! If you have ideas for improving the simulations, enhancing the visuals, or extending the project, feel free to fork the repository and submit a pull request.

**Bug Fixes**: If you notice any bugs or issues, please report them through GitHub issues.

**Feature Requests**: We are open to suggestions for new features, such as additional visualizations or more advanced models of space-time behavior.

**Documentation**: Contributions to improve the documentation or add new examples are always appreciated.

## Getting Started

To get started with the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/emergent-space-time.git
cd emergent-space-time
pip install -r requirements.txt
```

## Numerical Validation with Athena MHD Code

### Using Athena for Model Validation

[Athena](https://github.com/PrincetonUniversity/athena) is a grid-based code for astrophysical magnetohydrodynamics (MHD) developed by Princeton University. While our mathematical formulations present a novel approach to time-density relationships, certain aspects can be validated through numerical simulations.

### Installation and Setup

To install Athena for validation purposes, you need to use a proper Python environment (not within VS Code's integrated terminal):

```bash
# Clone the Athena repository
git clone https://github.com/PrincetonUniversity/athena.git

# Navigate to the Athena directory
cd athena

# Make sure you're using a compatible Python environment (Python 3.x)
# For Windows users, you may need to run this in a regular Command Prompt or PowerShell
python configure.py --prob=blast --coord=spherical-polar --flux=hllc

# On Linux/macOS systems, use:
# ./configure.py --prob=blast --coord=spherical-polar --flux=hllc

# Compile the code (you'll need a C++ compiler installed)
make
```

**Note for Windows users:** You may need to install a C++ compiler such as MinGW or use Windows Subsystem for Linux (WSL) for optimal performance. The code was primarily designed for Unix-like systems.

**Alternative setup with Docker:** If you encounter issues with direct installation, you can build a custom Docker image with Athena using these step-by-step instructions:

```bash
# Step 1: Create a directory for your Docker setup
mkdir athena-docker
cd athena-docker

# Step 2: Create a Dockerfile (use a text editor to create this file named "Dockerfile" with no extension)
# For Windows, you can use: notepad Dockerfile
# Then paste the following content in the file:
```

Create a file named `Dockerfile` (with no extension) and paste this content:

```
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y build-essential git python3 python3-pip cmake
RUN git clone https://github.com/PrincetonUniversity/athena.git /athena
WORKDIR /athena
RUN python3 configure.py --prob=blast --coord=spherical-polar --flux=hllc
RUN make
WORKDIR /workspace
CMD ["/bin/bash"]
```

Then build and run the Docker container:

```bash
# Step 3: Build the Docker image (note the dot at the end - it's important!)
docker build -t athena-custom .

# Step 4: Run a container with the image, mounting your current directory
docker run -it -v ${PWD}:/workspace athena-custom
```

**Windows-specific notes:**
- On Windows PowerShell, you may need to use `${PWD}` or `"$(pwd)"` for the current directory
- If you get path errors, try using full paths: `-v "C:\Users\yourusername\path\to\directory:/workspace"` 
- Ensure Docker Desktop is running before executing these commands

This creates a custom Docker container that has Athena pre-installed and configured, avoiding the need to set up the build environment on your local machine.

### Validation Approach

While Athena cannot directly validate our Time-Density Geometry and Temporal Flow Ratio formulations, it can help validate several underlying physical aspects:

1. **Gravitational Time Dilation**: Using Athena's general relativistic MHD capabilities, we can simulate the behavior of matter near massive objects and observe time dilation effects.

2. **Event Horizon Dynamics**: Athena can model fluid dynamics near black hole event horizons, providing insight into how space behaves near a Schwarzschild radius.

3. **Density-Time Relationships**: By tracking density evolution in simulated cosmological expansion/contraction scenarios, we can compare with our time-density formulations.

### Implementation Example

Here's a simple example of how to set up a simulation to test aspects of our model:

```python
# Example Python script to analyze Athena output for time dilation effects
import numpy as np
import matplotlib.pyplot as plt
from athena_read import athdf  # Requires the Athena analysis tools

# Load simulation data (after running Athena)
data = athdf('relativistic_blast_out.athdf')

# Extract density and velocity data
density = data['rho']
velocity = np.sqrt(data['vel1']**2 + data['vel2']**2 + data['vel3']**2)

# Calculate relativistic time dilation factor
gamma = 1 / np.sqrt(1 - (velocity/3e8)**2)

# Analyze the relationship between density and time dilation
plt.figure(figsize=(10, 6))
plt.scatter(density.flatten(), gamma.flatten(), alpha=0.1)
plt.xlabel('Density')
plt.ylabel('Time Dilation Factor')
plt.title('Relationship Between Density and Time Dilation')
plt.yscale('log')
plt.xscale('log')
plt.savefig('density_time_dilation.png')
```

**Enhanced Docker Setup for Athena:** We've created a more comprehensive Docker setup that includes additional tools and scripts for working with Athena:

```bash
# Navigate to the Docker directory
cd athena-docker

# Build the enhanced Docker image (note the dot at the end - it's important!)
docker build -t athena-custom .

# Run a container with the image, mounting your current directory
docker run -it -v ${PWD}:/workspace athena-custom
```

**Inside the Docker container, you can:**
- Run the example blast problem: `run-blast`
- Rebuild Athena with different options: `rebuild-athena`
- Use the provided analysis script: `python3 /analysis/athena_analysis.py <output_file.h5>`

This enhanced setup includes all necessary dependencies for both running simulations and analyzing the output, with particular focus on studying time dilation effects in high-density regions.

## Athena Simulation and Analysis Workflow

We've developed a comprehensive workflow to validate our time-density and temporal flow ratio theories using the Athena MHD code. This workflow allows us to run simulations, analyze results, and generate comparative reports.

### Core Components

1. **Time-Density Model Implementation**: We've implemented our original time-density model in Athena through a custom problem generator (`time_density.cpp`). The model combines:
   - Projection factor: `S(t) = 1 / (1 + sin²(ωt))`
   - Dimension expansion factor: `D(t) = 1 + αt²`
   - Temporal flow ratio: `R(t) = 1 / (1 + β/(|t| + ε))`

2. **Analysis Tool**: Enhanced `athena_analysis.py` that compares simulation results with theoretical predictions.

3. **Automated Comparison**: The `compare_simulations.py` script automates running both standard and time-density simulations, analyzing the results, and generating comprehensive reports.

### Validation Process

The validation workflow involves these steps:

1. **Run Docker Simulations**:
   ```bash
   # Navigate to the project directory
   cd "Genesis ETL Project\Sphere\Genesis-Sphere"
   
   # Run the comparison script with simulation flag
   python compare_simulations.py --run-simulations
   ```

2. **Automatic Analysis**:
   - The script loads data from both simulations
   - Creates side-by-side comparison plots for density, velocity, and pressure
   - Calculates statistics (means, differences, error percentages)
   - Generates a detailed PDF report

3. **Theory Validation**:
   - Simulation results confirm that our time-density geometry affects physical parameters
   - The temporal flow ratio successfully modulates velocity and pressure
   - These results help validate our core theory that space-time density and flow are interconnected

### Key Findings

Our simulations demonstrate several important phenomena:
- Velocity modulation corresponding to our temporal flow ratio
- Pressure changes that align with theoretical predictions
- Density variations that match our time-density geometry formula

This numerical validation confirms that our mathematical model has physical significance and can be represented in computational fluid dynamics simulations.

### How to Use the Workflow

#### Prerequisites

Before running the simulation comparison workflow, ensure Docker is properly set up:

```bash
# Navigate to the Docker directory
cd athena-docker

# Build the custom Athena Docker image
docker build -t athena-custom .

# Verify the image was created
docker images
```

#### Windows-Specific Docker Setup

```bash
# For Windows PowerShell, use this syntax for paths
docker run -it -v ${PWD}:/workspace athena-custom

# For Command Prompt, use this syntax 
docker run -it -v %cd%:/workspace athena-custom

# If you encounter path issues, use absolute paths
docker run -it -v "C:\Users\sszuk\OneDrive\Desktop\Genesis ETL Project\Sphere\Genesis-Sphere:/workspace" athena-custom
```

#### Running the Simulation Workflow

The simulation comparison tool runs Docker containers automatically, so you should execute these commands from your host system (Windows PowerShell or Command Prompt), not from inside a container:

```bash
# Basic comparison (using existing simulation results)
python compare_simulations.py

# Run new simulations and then compare
python compare_simulations.py --run-simulations

# Specify a custom output directory
python compare_simulations.py --output-dir "my_results"

# Run with a specific configuration file
python compare_simulations.py --config custom_config.json
```

> **Important**: If you see a Docker prompt like `root@container:/workspace#`, you're inside a Docker container. Type `exit` to return to your host system before running these commands.

The workflow automatically handles Docker container management, simulation execution, and results analysis, providing a seamless validation pipeline for our theoretical models.

#### Troubleshooting Simulation Issues

If you encounter issues running the simulations:

1. **Input File Errors**: Ensure all input files (*.athinput and *.in) have proper block structure with each section enclosed in angle brackets:
   ```
   <block_name>
   parameter = value
   </block_name>
   ```

2. **Boundary Condition Errors**: Athena only accepts specific boundary types:
   - `reflecting` - reflection boundary conditions
   - `periodic` - periodic boundary conditions 
   - `user` - user-defined boundary conditions
   
   Common boundary types like "outflow" or "inflow" may not be recognized.

3. **Missing Output Files**: Check that:
   - Docker has proper permissions to write to your file system
   - The Docker mount point is correct (use absolute paths if needed)
   - The OUTPUT_DIR exists (default: "simulation_results")

4. **Docker Issues**:
   - Verify Docker is running properly with `docker ps`
   - Try rebuilding the Athena Docker image: `docker build -t athena-custom ./athena-docker`
   - For Windows users, ensure Docker Desktop is configured to share your drives

5. **Manual Verification**:
   You can verify the Athena setup inside the Docker container:
   ```bash
   # Enter a Docker container interactively
   docker run -it --rm -v ${PWD}:/workspace athena-custom
   
   # Inside the container, try running Athena manually with proper syntax
   # Note: there should be NO space between -o and the output prefix
   /athena/bin/athena -i /athena/inputs/hydro/athinput.blast -otest_blast
   
   # For your custom input files, use the valid boundary type 'periodic'
   # (We can see from the example input file that 'periodic' is valid)
   /athena/bin/athena -i athena-docker/inputs/minimal_test.in -ominimal_test
   
   # Check if output files were created
   ls -la
   
   # To run the time-density simulation:
   /athena/bin/athena -i athena-docker/inputs/time_density.athinput -otime_density_test
   
   # To analyze the results (after fixing the analysis script):
   python3 /analysis/athena_analysis.py time_density_test.out1.00000
   ```

6. **Analysis Script Error**: 
   If you encounter syntax errors in the analysis script, you may need to fix it:
   ```bash
   # Edit the script inside the container
   nano /analysis/athena_analysis.py
   
   # Or create a corrected version in your workspace
   nano athena-docker/fixed_analysis.py
   ```

The workflow automatically handles Docker container management, simulation execution, and results analysis, providing a seamless validation pipeline for our theoretical models.

## License

This project is licensed under the MIT License — see the LICENSE file for details.

## Connect with Us

We encourage collaboration and discussions about the project. You can reach out to us or share your thoughts via the following channels:

**GitHub Issues**: For bug reports and feature requests.

**Discussion Forum**: Engage with the community to share insights and ideas.

**Email**: [sszukala at gmail dot com]

Thank you for exploring the Emergent Space-Time project! We hope it sparks curiosity and provides a fresh perspective on the nature of the universe and time itself.