import numpy as np

a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
J = []
for i in range(0, 10):
    for j in range(i+1, 10):
        b = a[:, i]  # 得到第i列数据
        c = a[:, j]  # 得到第j列数据
        d = np.cov(b, c)
        J.append(d[0][0])
e = max(J)  # 得到最大协方差值
f = min(J)  # 得到最小的协方差值
print("协方差最大值", e)
print("协方差最小值", f)