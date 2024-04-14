import numpy as np


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
    data = np.loadtxt('imu.txt', dtype=np.float32, delimiter=',')
    t = data[:, 6]
    print(t.size)
