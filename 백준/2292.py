import sys
n = int(sys.stdin.readline())
i = 1
answer = 1
while i < n:
    i += 6 * answer
    answer += 1

print(answer)