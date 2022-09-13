import sys

nums = list(map(int, sys.stdin.readline().split()))
n, m = nums[0], nums[1]
answer = []
hear = {}
for i in range(n):
    temp = sys.stdin.readline().strip()
    hear[temp] = 1
for i in range(m):
    temp = sys.stdin.readline().strip()
    if temp in hear:
        answer.append(temp)

print(len(answer))
for i in sorted(answer):
    print(i)