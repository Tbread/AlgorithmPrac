import math
import sys

f = math.factorial

repeat = int(input())
for rp in range(repeat):
    l = list(sys.stdin.readline().strip().split(' '))
    n = int(l[0])
    m = int(l[1])
    r = int(f(m) / (f(n) * f(m - n)))
    print(r)
