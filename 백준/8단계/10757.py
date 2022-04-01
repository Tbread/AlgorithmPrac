import sys
from collections import deque
inp = (sys.stdin.readline().strip()).split(' ')
#딱봐도 최대값은 넘어보임
a = inp[0]
b = inp[1]

if len(a) != len(b):
    if len(a) < len(b):
        tmp_l = len(b) - len(a)
        tmp_s = str(0) * tmp_l
        a = tmp_s+a
    else:
        tmp_l = len(a) - len(b)
        tmp_s = str(0) * tmp_l
        b = tmp_s+b

la = list(a)
lb = list(b)
arr = deque()
next = 0
for i in range(len(la)-1,-1,-1):
    tmp = int(la[i])+int(lb[i])+next
    if tmp >= 10:
        tmp = tmp - 10
        next = 1
    else:
        next = 0
    arr.appendleft(tmp)
if next == 1:
    arr.appendleft(1)
strs = ''
for i in range(len(arr)):
    strs = strs+str(arr[i])
print(strs)