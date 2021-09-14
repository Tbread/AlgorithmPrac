import sys
n = int(input())
l = sys.stdin.readline().strip().split(' ')
for i in range(len(l)):
    l[i]= int(l[i])
l.sort()
print(l[0]*l[-1])