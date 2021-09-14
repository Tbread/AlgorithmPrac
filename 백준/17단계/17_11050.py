import sys
import math
f = math.factorial
l = list(sys.stdin.readline().strip().split(' '))
n = int(l[0])
k = int(l[1])
result = f(n)/(f(k)*f(n - k))
print(int(result))