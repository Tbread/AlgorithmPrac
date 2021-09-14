import heapq
import sys
imheap = []

repeat = int(input())

for _ in range(repeat):
    order = int(sys.stdin.readline().strip())
    if not imheap and order == 0:
        print('0')
    elif order == 0:
        print(imheap[0])
        heapq.heappop(imheap)
    else:
        heapq.heappush(imheap,order)


