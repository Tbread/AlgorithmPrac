import sys
n = sorted(list(map(int,sys.stdin.readline().strip().split(' '))))
m = list(set(n))
answer = 0
if len(m) == 1:
    answer = 10000+(m[0]*1000)
elif len(m) == 2:
    answer = 1000+(n[1]*100)
else:
    answer = n[2]*100
print(answer)