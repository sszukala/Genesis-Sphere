// Time-Density Geometry Problem Generator for Athena++
// Implements the time-density function from the Genesis Sphere project

#include <cmath>
#include "athena.hpp"
#include "athena_arrays.hpp"
#include "mesh/mesh.hpp"
#include "parameter_input.hpp"
#include "coordinates/coordinates.hpp"
#include "hydro/hydro.hpp"
#include "eos/eos.hpp"

// Time-Density function exactly as described in our research paper
Real TimeDensity(Real t, Real alpha, Real omega) {
  // Projection factor from 4D → 3D (tesseract rotation)
  Real S_t = 1.0 / (1.0 + std::pow(std::sin(omega * t), 2));
  
  // Dimension expansion factor
  Real D_t = 1.0 + alpha * t * t;
  
  // Combined density (assumes V_shape = 1 for simplicity)
  return S_t * D_t;
}

// Temporal Flow Ratio function - models time flow near singularities
Real TemporalFlowRatio(Real t, Real beta, Real epsilon) {
  return 1.0 / (1.0 + beta / (std::abs(t) + epsilon));
}

// Problem generator function
void ProblemGenerator(MeshBlock *pmb, ParameterInput *pin) {
  // Get parameters from input file or use defaults
  Real alpha = pin->GetOrAddReal("problem", "alpha", 0.01);
  Real omega = pin->GetOrAddReal("problem", "omega", 1.0);
  Real beta = pin->GetOrAddReal("problem", "beta", 0.5);
  Real epsilon = pin->GetOrAddReal("problem", "epsilon", 0.001);
  Real t_init = pmb->pmy_mesh->time;
  Real pressure = pin->GetOrAddReal("problem", "pressure", 1.0);
  Real gamma_eos = pin->GetOrAddReal("hydro", "gamma", 5./3.);
  
  // Log the parameters for reference
  std::cout << "Time-Density Model Parameters:" << std::endl;
  std::cout << "  time = " << t_init << std::endl;
  std::cout << "  alpha = " << alpha << std::endl;
  std::cout << "  omega = " << omega << std::endl;
  std::cout << "  beta = " << beta << std::endl;
  std::cout << "  epsilon = " << epsilon << std::endl;
  
  // Calculate density using our time-density model
  Real rho = TimeDensity(t_init, alpha, omega);
  
  // Calculate temporal flow ratio
  Real flow_ratio = TemporalFlowRatio(t_init, beta, epsilon);
  std::cout << "  flow_ratio = " << flow_ratio << std::endl;
  
  // Access conserved variables array
  AthenaArray<Real> &u = pmb->phydro->u;
  
  // Initialize with uniform density and pressure, zero velocity
  for (int k = pmb->ks; k <= pmb->ke; ++k) {
    for (int j = pmb->js; j <= pmb->je; ++j) {
      for (int i = pmb->is; i <= pmb->ie; ++i) {
        u(IDN, k, j, i) = rho;
        u(IM1, k, j, i) = flow_ratio * 0.1;  // Velocity modulator in x-direction
        u(IM2, k, j, i) = 0.0;
        u(IM3, k, j, i) = 0.0;
        
        // Set energy (pressure / (gamma-1) + kinetic energy)
        Real pressure_modulated = pressure * flow_ratio;
        Real eint = pressure_modulated / (gamma_eos - 1.0);
        Real ek = 0.5 * rho * std::pow(flow_ratio * 0.1, 2);  // 0.5 * rho * v^2
        u(IEN, k, j, i) = eint + ek;
      }
    }
  }
}

// Optional: Add a refinement condition method if needed
// void RefinementCondition(MeshBlock *pmb) { ... }
