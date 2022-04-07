import sys
from collections import deque
global deque


def excute_deque(command):
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if not deq:
            print(-1)
        else:
            temp = deq.popleft()
            print(temp)
            deq.appendleft(temp)
    elif command[0] == 'back':
        if not deq:
            print(-1)
        else:
            temp = deq.pop()
            print(temp)
            deq.append(temp)


deq = deque()
counts = int(sys.stdin.readline())
for _ in range(counts):
    excute_deque(list(sys.stdin.readline().strip().split()))