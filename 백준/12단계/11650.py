
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

xyarr.sort(key=lambda x:(x[0],x[1]))
for rp in range(len(xyarr)):
    print(str(xyarr[rp][0])+' '+str(xyarr[rp][1]))