import sys
from collections import deque

repeat = int(sys.stdin.readline())
for _ in range(repeat):
    commands = sys.stdin.readline().strip()
    flag = 0
    n = int(sys.stdin.readline())
    temp_str = deque(eval(sys.stdin.readline().strip()))
    commands = commands.replace('RR', '')
    isRev = 0
    if commands.count('D') > n:
        print('error')
        continue
    for command in commands:
        if command == 'R':
            if isRev == 1:
                isRev = 0
            else:
                isRev = 1
        elif command == 'D':
            if isRev == 1:
                temp_str.pop()
            else:
                temp_str.popleft()
    if isRev == 1:
        print(str(list(reversed(temp_str))).replace(' ',''))
    else:
        print(str(list(temp_str)).replace(' ',''))
