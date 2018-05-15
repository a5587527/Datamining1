# !/usr/bin/python3'
import numpy as np


a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
n = a.shape[0]  # 获得矩阵的行数
b = np.mean(a, axis=0)  # 计算多元均值向量
z = a - b   # 矩阵中心化
print(np.cumsum(np.dot(z, z.T))/n)  # 计算外积
