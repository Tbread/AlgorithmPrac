# import sys
#
# l = list(sys.stdin.readline().strip().split(' '))
# trees = int(l[0])
# needt = int(l[1])
# gett = 0
# treelen = []
# l = list(sys.stdin.readline().strip().split(' '))
# for i in range(len(l)):
#     treelen.append(int(l[i]))
# treelen.sort()
# for cut in range(treelen[-1], 0, -1):
#     cut_len = 0
#     for countcut in range(len(treelen)):
#         if treelen[countcut] > cut:
#             cut_len += 1
#             treelen[countcut] -= 1
#     gett += cut_len
#     if gett >= needt:
#         print(cut)
#         break
#
# try1
#
# import sys
# import math
# pow = math.pow
#
# l = list(sys.stdin.readline().strip().split(' '))
# trees = int(l[0])
# needt = int(l[1])
# treelen = []
# l = list(sys.stdin.readline().strip().split(' '))
# for i in range(len(l)):
#     treelen.append(int(l[i]))
# treelen.sort()
# mid = int(treelen[-1] / 2)
# attempt = 1
# post_mid = -1
# while True:
#     gett = 0
#     for cut in range(trees):
#         if treelen[cut] > mid:
#             gett += treelen[cut] - mid
#             print(str(treelen[cut])+'의 나무를 잘라서 '+str(gett)+'의 나무를 가지고있는상태입니다')
#     if gett > needt:
#         attempt += 1
#         post_mid = mid
#         mid = post_mid + int(treelen[-1]/pow(2,attempt))
#         if post_mid == mid:
#             print('찾았다')
#             break
#         print('mid의값을 늘려봅니다.현재값: ' + str(mid))
#     elif gett < needt:
#         attempt += 1
#         post_mid = mid
#         mid = post_mid - int(treelen[-1]/pow(2,attempt))
#         if post_mid == mid:
#             print('찾았다')
#             break
#         print('mid의값을 줄여봅니다.현재값: ' + str(mid))
#     else:
#         print('값을 찾았습니다'+str(mid))
#         break
#
# 디버깅용 프린트 지우기전
# try2

# import sys
# import math
# pow = math.pow
#
# l = list(sys.stdin.readline().strip().split(' '))
# trees = int(l[0])
# needt = int(l[1])
# treelen = []
# l = list(sys.stdin.readline().strip().split(' '))
# for i in range(len(l)):
#     treelen.append(int(l[i]))
# treelen.sort()
# mid = int(treelen[-1] / 2)
# attempt = 1
# post_mid = -1
# while True:
#     gett = 0
#     for cut in range(trees):
#         if treelen[cut] > mid:
#             gett += treelen[cut] - mid
#     if gett > needt:
#         attempt += 1
#         post_mid = mid
#         mid = post_mid + int(treelen[-1]/pow(2,attempt))
#         if post_mid == mid :
#             print(mid)
#             break
#     elif gett < needt:
#         attempt += 1
#         post_mid = mid
#         mid = post_mid - int(treelen[-1]/pow(2,attempt))
#         if post_mid == mid:
#             #여기에만 0체크를 시켜주면됨
#             for i in range(mid):
#                 gett = 0
#                 flag = 0
#                 for cut in range(trees):
#                     gett += treelen[cut] - (mid-1)
#                 if gett >= needt:
#                     flag = 1
#             if flag == 1:
#                 print(mid-1)
#                 break
#             else:
#                 print(mid)
#                 break
#     else:
#         print(mid)
#         break
#
# try3 갈아엎자..

#
# import sys
#
# l = list(sys.stdin.readline().strip().split(' '))
# trees = int(l[0])
# needt = int(l[1])
# treelen = []
# l = list(sys.stdin.readline().strip().split(' '))
# for i in range(len(l)):
#     treelen.append(int(l[i]))
# treelen.sort()
# sp = 0
# ep = treelen[-1]
#
# while sp <= ep:
#     mid = int((sp + ep) / 2)
#     gett = 0
#     for i in treelen:
#         if i > mid:
#             gett += i - mid
#     if gett >= needt:
#         sp = mid + 1
#     else:
#         ep = mid - 1
# print(ep)
#
#
# try4 왜시간초과일까 나무수가많으면 길이할당에 시간을 오래써서?

import sys

l = list(sys.stdin.readline().strip().split(' '))
trees = int(l[0])
needt = int(l[1])
treelen = list(map(int,input().split()))
treelen.sort()
sp = 0
ep = treelen[-1]

while sp <= ep:
    mid = int((sp + ep) / 2)
    gett = 0
    for i in treelen:
        if i > mid:
            gett += i - mid
    if gett >= needt:
        sp = mid + 1
    else:
        ep = mid - 1
print(ep)

#python3로 제출하면 여전히 시간초과인데 똑같이 pypy3로 제출하면 성공한다.어디서 시간을 더 줄일수있는거지?