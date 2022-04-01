import sys,itertools

n,m = map(int,sys.stdin.readline().strip().split(' '))
arr = []
for i in range(1,n+1):
    arr.append(i)

products = itertools.product(arr,repeat=m)
for product in products:
    temp_str = ''
    for ele in product:
        temp_str += str(ele) + ' '
    print(temp_str.strip())