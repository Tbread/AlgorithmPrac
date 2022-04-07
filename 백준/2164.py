import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque()

for i in range(n,0,-1):
    stack.append(i)

while len(stack) != 1:
    stack.pop()
    temp = stack.pop()
    stack.appendleft(temp)

print(stack.pop())