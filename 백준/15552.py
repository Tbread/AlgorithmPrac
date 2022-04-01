import sys
a = int(input())

for i in range(a):
    l = (sys.stdin.readline().strip()).split(' ')
    print(int(l[0])+int(l[1]))
