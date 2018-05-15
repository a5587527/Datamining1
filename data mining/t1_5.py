# !/usr/bin/python3'
import numpy as np
import scipy.stats as st
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = []
print(a.shape[0])  # 获得行数
b = a[:, 0]
print(b.var())
c = float(np.max(b)-np.min(b))/a.shape[0]  # 获得步长，为了精确强制转换为float
x = np.arange(np.min(b), np.max(b), c)
loc = (np.max(b)+np.min(b))/2  # 获得均值
scala = b.var()  # 获得方差
y = st.norm.pdf(x, loc, scala)  # 统计函数库script
plot(x, y)
show()
