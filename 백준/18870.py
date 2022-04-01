import sys
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().strip().split(' ')))
dict = {}
v = sorted(list(set(m)))

for i in range(len(v)):
    dict[v[i]] = i

for ele in m:
    print(dict[ele])