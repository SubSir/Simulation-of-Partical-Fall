import numpy as np
import copy

# Constants
g = 9.8  # Acceleration due to gravity (m/s^2)
rho_air = 1.2  # Density of air (kg/m^3)
viscosity = 1.8e-5  # Viscosity of air (kg/(m*s))

def simulate_particle_fall(mass, diameter, initial_velocity, height):
  step_time = 0.01  # Time step for simulation (s), change it when you find the velocity is too large
  # Calculate forces  
  gravity_force = mass * g
  buoyancy_force = (4/3) * np.pi * (diameter/2)**3 * g * rho_air
  
  # The critical situation for the Dragula formula and Stokes' formula is approximately when the forces from both are the same.
  drag_force = max(6 * np.pi * (diameter/2) * viscosity * initial_velocity,
                   0.4* 0.5 * rho_air * (initial_velocity**2) * np.pi * (diameter/2)**2)

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
    drag_force = max(6 * np.pi * (diameter/2) * viscosity * velocity,
                     0.4* 0.5 * rho_air * (velocity**2) * np.pi * (diameter/2)**2)
    acceleration = (gravity_force - buoyancy_force - drag_force) / mass

  return time

def simulate_particle_fall2(mass, diameter, max_time,  x_position, x_velocity, y_position,y_velocity, z_position, z_velocity):

  step_time = 0.01  # Time step for simulation (s), change it when you find the velocity is too large
  # Calculate forces
  gravity_force = mass * g
  buoyancy_force = (4/3) * np.pi * (diameter/2)**3 * g * rho_air
  velocity = (x_velocity**2 + y_velocity**2 + z_velocity**2)**0.5
  drag_force = max(6 * np.pi * (diameter/2) * viscosity * velocity,
                     0.4* 0.5 * rho_air * (velocity**2) * np.pi * (diameter/2)**2)

  # Calculate acceleration
  if velocity == 0:
    z_acceleration = (gravity_force - buoyancy_force - drag_force) / mass
    x_acceleration = 0
  else:
    z_acceleration = (gravity_force - buoyancy_force - drag_force * z_velocity / velocity) / mass
    x_acceleration = - drag_force * x_velocity / velocity / mass

  # Simulate particle fall
  time = 0
  position = [x_position, y_position, z_position]
  
  times = []
  positions = []

  while max_time >= time:
    times.append(time)
    positions.append(position.copy())
    
    # Update position and velocity
    p0 = position[0]
    p1 = position[1]
    x0 = x_velocity
    z0 = z_velocity
    
    position[0] += x_velocity * step_time 
    position[2] -= z_velocity * step_time + 0.5 * z_acceleration * step_time**2
    x_velocity += x_acceleration * step_time
    z_velocity += z_acceleration * step_time
    
    while(x_velocity >=0 and step_time < 0.01):
      position[0] = p0
      position[1] = p1
      x_velocity = x0
      z_velocity = z0
      step_time = step_time * 2
      position[0] += x_velocity * step_time
      position[2] -= z_velocity * step_time + 0.5 * z_acceleration * step_time**2
      x_velocity += x_acceleration * step_time
      z_velocity += z_acceleration * step_time
      
    while(x_velocity <0):
      position[0] = p0
      position[1] = p1
      x_velocity = x0
      z_velocity = z0
      step_time = step_time / 2
      position[0] += x_velocity * step_time 
      position[2] -= z_velocity * step_time + 0.5 * z_acceleration * step_time**2
      x_velocity += x_acceleration * step_time
      z_velocity += z_acceleration * step_time
    
    if position[2] < 0:
      z_velocity = -z_velocity
      position[2] = 0
    velocity = (x_velocity**2 + y_velocity**2 + z_velocity**2)**0.5
    
    # Update time
    time += step_time # Time step of 0.01 seconds
    
    # Update forces and acceleration
    drag_force = max(6 * np.pi * (diameter/2) * viscosity * velocity,
                     0.4* 0.5 * rho_air * (velocity**2) * np.pi * (diameter/2)**2)

    z_acceleration = (gravity_force - buoyancy_force - drag_force * z_velocity / velocity) / mass
    x_acceleration = - drag_force * x_velocity / velocity / mass

  return times, positions

# Example usage
'''mass = 0.01  # Mass of the particle (kg)
diameter = 0.001  # Diameter of the particle (m)
initial_velocity = 0  # Initial velocity of the particle (m/s)

fall_time = simulate_particle_fall(mass, diameter, initial_velocity, 1)
print("Particle fall time:", fall_time, "seconds")'''