import sys,itertools

n,m = map(int,sys.stdin.readline().strip().split(' '))
arr = []
for i in range(1,n+1):
    arr.append(i)

combs = itertools.combinations_with_replacement(arr,m)
for comb in combs:
    temp_str = ''
    for ele in comb:
        temp_str += str(ele) + ' '
    print(temp_str.strip())