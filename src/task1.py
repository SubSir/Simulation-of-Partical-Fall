# Import necessary libraries
import particle_fall
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
diameters = np.arange(0.001, 0.051, 0.001)  # m
density = 10  # kg/m^3
height = 1  # m
initial_velocity = 0  # m/s

# Initialize an empty list to store the fall times
fall_times = []

# Iterate over the diameters
for diameter in diameters:
  # Calculate the mass based on density and diameter
  mass = density * (np.pi * diameter**3) / 6
  
  # Call the simulate_particle_fall function
  time = particle_fall.simulate_particle_fall(mass, diameter, initial_velocity, height)
  
  # Append the fall time to the list
  fall_times.append(time)
  
  print(f'Particle with diameter {diameter} m took {time} s to fall')

# Plot the results
plt.plot(diameters, fall_times)
plt.xlabel('Diameter (m)')
plt.ylabel('Time (s)')
plt.title('Particle Fall Time')
plt.show()