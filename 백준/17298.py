import sys
from collections import deque

n = int(sys.stdin.readline().strip())

arr = deque(map(int,sys.stdin.readline().strip().split()))
answer = []
for i in range(n):
    standard = arr[i]
    if i == n-1:
        answer.append(-1)
        break
    temp_d = deque(arr[i + 1:])
    for j in range(len(temp_d)):
        temp = temp_d.popleft()
        if temp > standard:
            answer.append(temp)

print(answer)
