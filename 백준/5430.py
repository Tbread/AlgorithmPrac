import sys
from collections import deque

repeat = int(sys.stdin.readline())
for _ in range(repeat):
    commands = sys.stdin.readline().strip()
    flag = 0
    n = int(sys.stdin.readline())
    temp_str = sys.stdin.readline().strip('[').strip().strip(']')
    if temp_str:
        deq = deque(map(int, temp_str.split(',')))
    else:
        deq = deque()
    prev_commands = ''
    while True:
        if prev_commands == commands:
            break
        prev_commands = commands
        commands = commands.replace('RR','')
    for command in commands:
        if command == 'D':
            if not deq:
                print('error')
                flag = 1
                break
            else:
                deq.popleft()
        else:
            deq.reverse()
    if flag == 1:
        continue
    print(deq)
