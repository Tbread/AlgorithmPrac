import sys
n = list(map(int,sys.stdin.readline().strip().split(' ')))
n[1] += int(sys.stdin.readline().strip())
if n[1] >= 60:
    n[0] += int(n[1] / 60)
    while n[1] >= 60:
        n[1] -= 60
if n[0] >= 24:
    n[0] -= 24
print(str(n[0])+' '+str(n[1]))