from math import *
import numpy as np

#fonction:

f = lambda x : 1 / x

def riemman_sum( n, a, b):
    w = (b - a) / n
    x_0 = a
    s = f(x_0)
    for i in range(1, n):
        s = s + f(x_0 + i * w)
    
    s = w * s
    return s

res = riemman_sum(3, 1, 4)
print(res)


# R = sum (delta x f(t_i)) ~= integrale ( f(t) dt) entre [a,b]