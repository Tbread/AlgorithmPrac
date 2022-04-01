# import sys
# repeat = int(input())
# arr = []
# for _ in range(repeat):
#     a = sys.stdin.readline().strip().split(' ',1)
#     arr.append(a)
# arr.sort(key=lambda x:(x[0]))
#
# for i in arr:
#     print(*i)
#
#으아악 왜안돼

import sys
repeat = int(input())
arr = []
for _ in range(repeat):
    a = sys.stdin.readline().strip().split(' ',1)
    arr.append(a)
arr.sort(key=lambda x:int(x[0]))

for i in arr:
    print(*i)

#안됐던이유 : 인트안붙임....
