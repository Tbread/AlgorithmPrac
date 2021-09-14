import sys
N = int(input())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
arr = list(set(arr))
arr.sort(key=lambda x:(len(x),x))
for i in arr:
    print(i)