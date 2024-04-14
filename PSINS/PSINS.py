import numpy as np
import matplotlib.pyplot as plt
import math

data_imu = np.loadtxt('imu.txt', dtype=np.float32, delimiter=',')
data_alt = np.loadtxt('avp.txt', dtype=np.float32, delimiter=',')

t = data_imu[:, 6]

wx = data_imu[:, 0]
wy = data_imu[:, 1]
wz = data_imu[:, 2]

ax = data_imu[:, 3]
ay = data_imu[:, 4]
az = data_imu[:, 5]

pitch = data_alt[:, 0]
roll = data_alt[:, 1]
yaw = data_alt[:, 2]

VE = data_alt[:, 3]
VN = data_alt[:, 4]
VU = data_alt[:, 5]

lat = data_alt[:, 6]
lon = data_alt[:, 7]
alt = data_alt[:, 8]


