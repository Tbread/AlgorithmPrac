import sys,itertools

n,m = map(int,sys.stdin.readline().strip().split(' '))
arr = []
for i in range(1,n+1):
    arr.append(i)

perms = itertools.permutations(arr,m)

for perm in perms:
    temp_str = ''
    for ele in perm:
        temp_str += str(ele) + ' '
    print(temp_str.strip())