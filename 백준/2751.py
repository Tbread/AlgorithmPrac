import sys, heapq

arr = []
N = int(input())
for i in range(N):
    arr.append(int(sys.stdin.readline()))

heapq.heapify(arr)
for i in range(N):
    print(heapq.heappop(arr))
