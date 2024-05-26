# Import necessary libraries
import particle_fall
import multiple_partical_fall
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio.v2 as imageio
import os

diameter = 0.001  # m
density = 1000  # kg/m^3
heights = np.arange(0, 1, 0.1)  # m
initial_velocity = 0  # m/s
max_time = 4  # s
mass = density * (np.pi * diameter**3) / 6

x_velocitys = [0.5, 5, 25, 50]
x_max = [2, 7, 13, 13]
time_sequence = np.arange(0, max_time, 0.1)

for ii in range(len(x_velocitys)):
  x_velocity = x_velocitys[ii]
  filenames = []
  for index in range(len(time_sequence)):
    ask_time = time_sequence[index]
    
    positions = []
    times = []

    answer_x = []
    answer_y = []
    answer_z = []

    for height in heights:
      for i in heights:
        for j in heights:
          time, position = particle_fall.simulate_particle_fall3(mass, diameter, max_time, i, x_velocity, j, 0, height, 0)
          for t in range(len(position)):
            if (time[t] >= ask_time):
              answer_x.append(position[t][0])
              answer_y.append(position[t][1])
              answer_z.append(position[t][2])
              break
            
    # 创建一个新的图形
    fig = plt.figure()

    # 创建一个3D坐标轴
    ax = fig.add_subplot(111, projection='3d')

    # 使用scatter方法绘制3D散点图
    ax.scatter(answer_x, answer_y, answer_z)

    ax.set_xlim(0, x_max[ii])
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)

    filename = f'frame_{index}.png'
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

  # 使用图像序列创建GIF
  with imageio.get_writer('task3_' + str(ii) + '.gif', mode='I') as writer:
      for filename in filenames:
          image = imageio.imread(filename)
          writer.append_data(image)

  # 删除图像文件
  for filename in filenames:
      os.remove(filename)