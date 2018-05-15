# !/usr/bin/python3'
import numpy as np

a = np.loadtxt('magic04.txt',  delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
print(b)