import heapq
import sys
imheap = []

repeat = int(input())

for _ in range(repeat):
    order = int(sys.stdin.readline().strip()) #입력값이 많을땐 까먹지말고 input을 sys readline으로바꾸자...시간초과난다
    if not imheap and order == 0:
        print('0')
    elif order == 0:
        print(-imheap[0])
        heapq.heappop(imheap)
    else:
        heapq.heappush(imheap,-order)

#최대힙을 사용할땐 부호를 바꿔서넣고 출력할때 다시 부호를 바꾸자
