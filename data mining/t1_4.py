# !/usr/bin/python3'
import numpy as np
from matplotlib.pyplot import scatter
from matplotlib.pyplot import show
a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = a[:, 0]  # 取出属性一
c = a[:, 1]  # 取出属性二
covariance = np.cov(b, c)
corrc = np.corrcoef(b, c)  # 计算相关系数矩阵
print(corrc)
scatter(b, c,20,b,".")  # 绘制散点图
show()