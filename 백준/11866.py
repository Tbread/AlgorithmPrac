from collections import deque
import sys
arr = deque()
josep = []
nk = list(sys.stdin.readline().strip().split(' '))
N = int(nk[0])
K = int(nk[1])
for i in range(1,N+1):
    arr.append(i)
while len(arr) > 0:
    arr.rotate(-K+1)
    josep.append(arr[0])
    arr.popleft()

print('<',end='')
for i in josep:
    if i == josep[-1]:
        print(i,end='')
    else:
        print(i,end=', ')
print('>')

#rotate를 생각한덕분에 굉장히 빨리끝났다