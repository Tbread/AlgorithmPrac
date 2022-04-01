from collections import Counter
from collections import deque
import sys
repeat = int(input())
inp = deque()
mostlist = deque()
sum = 0
for rp in range(repeat):
    inp.append((int(sys.stdin.readline())))
    #inp.append(int(input()))
    sum += inp[rp]
inp = sorted(inp)
temp = Counter(inp).most_common()
temp = sorted(temp, key=lambda i:(-i[1],i[0]))
if len(temp) > 1 and temp[0][1] == temp[1][1]:
    mode = temp[1][0]
else:
    mode = temp[0][0]
# #     for i in range(len(temp)):
# #         if i > 0:
# #             if temp[i][1] != temp[i-1][1]:
# #                 break
# #         mostlist.append(temp[i][0])
# #     mode = mostlist[1]
# mostlist = sorted(mostlist)
aver = round(sum/repeat)
mid = inp[repeat//2]
rng = inp[-1] - inp[0]
print(aver)
print(mid)
print(mode)
print(rng)