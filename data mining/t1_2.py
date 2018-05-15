# !/usr/bin/python3'
import numpy as np


a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)  # 第一问的均值
n = a.shape[0]  # 获得行数
z = a-b  # 中心数据矩阵
print(np.dot(z.T, z)/n)