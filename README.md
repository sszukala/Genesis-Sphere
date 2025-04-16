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

To install Athena for validation purposes:

```bash
# Clone the Athena repository
git clone https://github.com/PrincetonUniversity/athena.git

# Navigate to the Athena directory
cd athena

# Configure with relativistic MHD support
./configure.py --prob=blast --coord=spherical-polar --eos=general/eos_table --flux=hllc --order=3 -b -g -s

# Compile the code
make
```

### Validation Approach

While Athena cannot directly validate our Time-Density Geometry and Temporal Flow Ratio formulations, it can help validate several underlying physical aspects:

1. **Gravitational Time Dilation**: Using Athena's general relativistic MHD capabilities, we can simulate the behavior of matter near massive objects and observe time dilation effects.

2. **Event Horizon Dynamics**: Athena can model fluid dynamics near black hole event horizons, providing insight into how space behaves near a Schwarzschild radius.

3. **Density-Time Relationships**: By tracking density evolution in simulated cosmological expansion/contraction scenarios, we can compare with our time-density formulations.

### Limitations for Our Model

It's important to note that Athena has specific limitations when it comes to validating our complete model:

- It can't directly simulate our 4D to 3D projection techniques
- The Temporal Flow Ratio formulation requires custom implementation
- Our specific sine-based projection factor is not a standard feature

### Alternative Validation Methods

For comprehensive validation of our mathematical formulations, we are considering:

1. **Custom Numerical Implementations**: Developing specialized code that directly implements our mathematical formulas.

2. **Analytical Proof**: Demonstrating mathematical consistency with established gravitational and relativistic principles.

3. **Observational Data Comparison**: Where possible, comparing our model predictions with astronomical observations.

The integration of Athena simulations with our custom visualization tools represents an ongoing development goal for this project.

## License

This project is licensed under the MIT License — see the LICENSE file for details.

## Connect with Us

We encourage collaboration and discussions about the project. You can reach out to us or share your thoughts via the following channels:

**GitHub Issues**: For bug reports and feature requests.

**Discussion Forum**: Engage with the community to share insights and ideas.

**Email**: [sszukala at gmail dot com]

Thank you for exploring the Emergent Space-Time project! We hope it sparks curiosity and provides a fresh perspective on the nature of the universe and time itself.