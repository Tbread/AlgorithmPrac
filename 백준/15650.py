# arr = [1,2,3,4,5]
# a = list(combinations(arr,3))
# print(a)
# #[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)] 반환
import sys
from itertools import combinations
inp = list(map(int, sys.stdin.readline().split()))
n = inp[0]
m = inp[1]

arr = list(range(1,n+1))
if m == 1:
    for i in range(len(arr)):
        print(arr[i])
else:
    a = list(combinations(arr,m))
    for i in range(len(a)):
        printing = ''
        for j in range(len(a[i])):
            printing = printing +' '+ str(a[i][j])
        print(printing.lstrip())