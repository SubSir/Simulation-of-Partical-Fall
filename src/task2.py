# Import necessary libraries
import particle_fall
import multiple_partical_fall
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio.v2 as imageio
import os

diameter = 0.001  # m
density = 10  # kg/m^3
heights = np.arange(0, 1, 0.1)  # m
initial_velocity = 0  # m/s
max_time = 4  # s

time_sequence = np.arange(0, max_time, 0.5)

filenames = []
for index in range(len(time_sequence)):
  ask_time = time_sequence[index]
  
  positions = []

  answer_x = []
  answer_y = []
  answer_z = []

  for height in heights:
    # Calculate the mass based on density and diameter
    mass = density * (np.pi * diameter**3) / 6
    
    # Call the simulate_particle_fall function
    
    for i in heights:
      diameter = 0.001
      for j in heights:
        time, position = particle_fall.simulate_particle_fall2(mass, diameter, max_time, 0, 0, 0, 0, height, 0)
        diameter += 0.01
        mass = density * (np.pi * diameter**3) / 6
        for k in range(len(position)):
          if time[k] >= ask_time:
            answer_x.append(i)
            answer_y.append(j)
            answer_z.append(position[k][2])
            positions.append([i, j, position[k][2]])
            break
  
  number_density = multiple_partical_fall.number_density(positions, [0.5, 0.5, 0.5])

  print(f'Number density at time {ask_time} s: {number_density}')
  
  # 创建一个新的图形
  fig = plt.figure()

  # 创建一个3D坐标轴
  ax = fig.add_subplot(111, projection='3d')

  # 使用scatter方法绘制3D散点图
  ax.scatter(answer_x, answer_y, answer_z)

  ax.set_xlim(0, 1)
  ax.set_ylim(0, 1)
  ax.set_zlim(0, 1)

  filename = f'frame_{index}.png'
  plt.savefig(filename)
  filenames.append(filename)
  plt.close()
'''
# 使用图像序列创建GIF
with imageio.get_writer('task2.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# 删除图像文件
for filename in filenames:
    os.remove(filename)

heights = np.arange(0, 1, 0.05)  # m
number_densitys = []

for index in range(len(time_sequence)):
  ask_time = time_sequence[index]
  
  positions = []

  for height in heights:
    # Calculate the mass based on density and diameter
    mass = density * (np.pi * diameter**3) / 6
    
    # Call the simulate_particle_fall function
    
    for i in heights:
      diameter = 0.001
      for j in heights:
        time, position = particle_fall.simulate_particle_fall2(mass, diameter, max_time, 0, 0, 0, 0, height, 0)
        diameter += 0.01
        mass = density * (np.pi * diameter**3) / 6
        for k in range(len(position)):
          if time[k] >= ask_time:
            positions.append([i, j, position[k][2]])
            break
  
  number_density = multiple_partical_fall.number_density(positions, [0.5, 0.5, 0.5])

  print(f'Number density at time {ask_time} s: {number_density}')
  number_densitys.append(number_density)

plt.plot(time_sequence, number_densitys)
plt.xlabel('Time (s)')
plt.ylabel('Number Density')
plt.title('Number Density vs Time')
plt.show()
'''