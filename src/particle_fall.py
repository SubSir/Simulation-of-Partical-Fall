import numpy as np

def simulate_particle_fall(mass, diameter, initial_velocity, height):
  # Constants
  g = 9.8  # Acceleration due to gravity (m/s^2)
  rho_air = 1.2  # Density of air (kg/m^3)
  viscosity = 1.8e-5  # Viscosity of air (kg/(m*s))
  step_time = 0.01  # Time step for simulation (s)

  # Calculate forces
  gravity_force = mass * g
  buoyancy_force = (4/3) * np.pi * (diameter/2)**3 * g * rho_air
  drag_force = 6 * np.pi * (diameter/2) * viscosity * initial_velocity

  # Calculate acceleration
  acceleration = (gravity_force - buoyancy_force - drag_force) / mass

  # Simulate particle fall
  time = 0
  position = height
  velocity = initial_velocity

  while position >= 0:
    # Update position and velocity
    position -= velocity * step_time + 0.5 * acceleration * step_time**2
    velocity += acceleration * step_time

    # Update time
    time += step_time # Time step of 0.01 seconds
    
    # Update forces and acceleration
    drag_force = 6 * np.pi * (diameter/2) * viscosity * velocity
    acceleration = (gravity_force - buoyancy_force - drag_force) / mass

  return time

# Example usage
'''mass = 0.01  # Mass of the particle (kg)
diameter = 0.001  # Diameter of the particle (m)
initial_velocity = 0  # Initial velocity of the particle (m/s)

fall_time = simulate_particle_fall(mass, diameter, initial_velocity, 1)
print("Particle fall time:", fall_time, "seconds")'''