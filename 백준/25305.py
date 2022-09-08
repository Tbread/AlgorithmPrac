import sys
from collections import deque

n,k = sys.stdin.readline().strip().split()
n,k = int(n),int(k)
arr = deque(list(map(int,sys.stdin.readline().strip().split())))

for i in range(k+1):
    answer = arr.pop()
print(answer)