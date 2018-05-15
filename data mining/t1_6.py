import numpy as np

a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = a.var(axis=0)
print(b)
print("最大值")
print(b.max())
print("最小值")
print(b.min())
