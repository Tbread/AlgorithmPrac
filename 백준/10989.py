import sys

arr = [0] * 10001

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    arr[m] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)