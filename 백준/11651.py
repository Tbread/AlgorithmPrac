# import sys
# repeat = int(input())
# xyarr = []
# yxarr = []
# for rp in range(repeat):
#     l = sys.stdin.readline().strip()
#     xyarr.append(l)
#     l =' '.join(reversed(l.split()))
#     yxarr.append(l)
# yxarr.sort()
#
import sys
repeat = int(input())
xyarr = []
# yxarr = []
for rp in range(repeat):
    l = list(sys.stdin.readline().strip().split(' '))
    xyarr.append(l)
for rp in range(len(xyarr)):
    xyarr[rp][0] = int(xyarr[rp][0])
    xyarr[rp][1] = int(xyarr[rp][1])
    # yxarr.append(list(reversed(xyarr[rp])))
    # yxarr.append(list(reversed(xyarr[rp])))
# print(xyarr)
# print(yxarr)
#
# yxarr.sort(key=lambda x:(x[0],x[1]))
# print(yxarr)
xyarr.sort(key=lambda x:(x[1],x[0]))
# print(xyarr)
for rp in range(len(xyarr)):
    print(str(xyarr[rp][0])+' '+str(xyarr[rp][1]))