import sys
from collections import deque
repeat = int(input())
dequeA = deque()
for rp in range(repeat):
    order = list(sys.stdin.readline().strip().split(' '))
    if order[0] == 'push':
        dequeA.append(order[1])
    elif order[0] == 'pop':
        if len(dequeA) == 0:
            print(-1)
        else:
            temp_value = dequeA[0]
            dequeA.popleft()
            print(temp_value)
    elif order[0] == 'size':
        print(len(dequeA))
    elif order[0] == 'empty':
        if len(dequeA) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(dequeA) == 0:
            print(-1)
        else:
            print(dequeA[0])
    elif order[0] == 'back':
        if len(dequeA) == 0:
            print(-1)
        else:
            print(dequeA[-1])