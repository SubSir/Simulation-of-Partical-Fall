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
total_time = 0

# Iterate over the diameters
for diameter in diameters:
  # Calculate the mass based on density and diameter
  mass = density * (np.pi * diameter**3) / 6
  
  # Call the simulate_particle_fall function
  time = particle_fall.simulate_particle_fall(mass, diameter, initial_velocity, height)
  
  # Append the fall time to the list
  fall_times.append(time)
  total_time += time
  
  #print(f'Particle with diameter {diameter} m took {time} s to fall')
  th = (10 - 1.2) * 9.8 * diameter**2 / 18 / 0.00018 * (time + diameter **2 *10 / 18 / 0.00018 * np.exp(-18 * 0.00018 * time / diameter **2 / 1.2))
  print(f'By theroical calculation, Particle with diameter {diameter} m should fall {th} m')

print(f'average time: {total_time/len(diameters)}')

# Plot the results
plt.plot(diameters, fall_times)
plt.xlabel('Diameter (m)')
plt.ylabel('Time (s)')
plt.title('Particle Fall Time')
plt.show()