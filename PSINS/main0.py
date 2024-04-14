import numpy as np
import matplotlib.pyplot as plt

GM = 3.986004415e14
Re = 6.378136998405e6
f = 1/298.257
wie = 9.2921151467e-5
g0 = 9.7803267714

def ReadData():
    data_imu = np.loadtxt('imu.txt', dtype=np.float32, delimiter=',')
    data_alt = np.loadtxt('avp.txt', dtype=np.float32, delimiter=',')

    t = data_imu[:, 6]
    len = t.size

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
    return [t, len, wx, wy, wz, ax, ay, az, pitch, roll, yaw, VE, VN, VU, lat, lon, alt]


def Vec2Mat(Vec):
    vx = Vec[0, 0]
    vy = Vec[1, 0]
    vz = Vec[2, 0]
    Mat = np.matrix([[0, -vz, vy], [vz, 0, -vx], [-vy, vx, 0]], dtype=float)
    return Mat


def QuaMulti(qua1, qua2):
    p0 = qua1[0, 0]
    p1 = qua1[1, 0]
    p2 = qua1[2, 0]
    p3 = qua1[3, 0]
    P = np.matrix([[p0, -p1, -p2, -p2], [p1, p0, -p3, p2], [p2, p3, p0, -p1], [p3, -p2, p1, p0]], dtype=float)
    return P * qua2


def QuaNorm(qua):
    p0 = qua[0, 0]
    p1 = qua[1, 0]
    p2 = qua[2, 0]
    p3 = qua[3, 0]
    sum = pow((pow(p0, 2) + pow(p1, 2) + pow(p2, 2) + pow(p3, 2)), 0.5)
    p0 = p0 / sum
    p1 = p1 / sum
    p2 = p2 / sum
    p3 = p3 / sum
    qua[0, 0] = p0
    qua[1, 0] = p1
    qua[2, 0] = p2
    qua[3, 0] = p3


if __name__ == '__main__':
    print(Re)
