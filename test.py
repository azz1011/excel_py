import math
from re import X
from math import sqrt

class test:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

def khoang_cach(a, b): 
    q= (a.x - b.x)*(a.y-b.y)
    print (q)


print ("nhap toa do diem A:")
a = test(float (input()), float(input()))

print ("nhap toa do diem B:")
b = test(float (input()), float(input()))

print(khoang_cach(a,b))
