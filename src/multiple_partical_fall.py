import numpy as np

def distance(x1, y1, z1, x2, y2, z2):
  return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2) ** 0.5

def distance(position1, position2):
  return ((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2 + (position1[2] - position2[2])**2) ** 0.5

def number_density(times, positions, time, position):
  min_distance = 0.01
  
  pos= 0
  for i in range(len(times)):
    if times[i] == time:
      pos = i
      break
    
  count = 0
  
  for i in range(positions[pos]):
    if distance(positions[pos][i], position) <= min_distance:
      count += 1
  return count / (4/3 * np.pi * min_distance**3)