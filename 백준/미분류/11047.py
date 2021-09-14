import sys
from collections import deque
nk = list(sys.stdin.readline().strip().split(' '))
N = int(nk[0])
K = int(nk[1])
need = []
all = []
balance = K
c = 0
for _ in range(N):
    all.append(int(sys.stdin.readline().strip()))
for i in range(len(all)):
    if all[i] <= K:
        need.append(all[i])
    else:
        break
arr = sorted(need,reverse=True)
deq = deque()
for i in arr:
    deq.append(i)

idx = 0
while balance > 0:
    if balance >= deq[0]:
        a = balance // deq[0] #일일히 한개씩 빼주니 시간초과가 나왔다. 한번에 빼버리자
        balance = balance - (deq[0]*a)
        c += a
    elif balance < deq[0]:
        deq.popleft()
print(c)
