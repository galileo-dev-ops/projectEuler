import math


def lcmFind(a, b):
    return abs(a * b) // math.gcd(a, b)


num = 1
for i in range(1, 21):
    num = lcmFind(num, i)

print(num)
