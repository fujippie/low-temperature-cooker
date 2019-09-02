import numpy as np
from matplotlib import pyplot as plt
from numpy.random import *
M = 0.00
M1 = 0.00
goal = 50.00
e = 0.00
e1 = 0.00
e2 = 0.00
Kp = 0.1
Ki = 0.1
Kd = 0.1

t = 100


x_list = []
y_list = []

x_list.append(0)
y_list.append(0.00)


for i in range(1, t):
        M1 = M
        e2 = e1
        e1 = e
        e = goal - y_list[i-1]  # 偏差（e） = 目的値（goal） - 前回の操作量

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))

        x_list.append(i)
        y_list.append(M)


plt.plot(x_list, y_list)
plt.ylim(0, goal*2)  # 見やすくするため
plt.show()
