# import sys
# from collections import deque
# #시간초과떠서 덱으로바꿈
#
# chkarr = []
# result = []
# arr = deque()
#
#
#
# repeat = int(input())
# for rp in range(repeat):
#     a = int(sys.stdin.readline()) #시간초과떠서 입력방식바꿈
#     if not arr and not chkarr:
#         arr = list(range(1,a+1))
#         for i in range(1, a + 1):
#             result.append('+')
#             chkarr.append(i)
#         arr.pop()
#         result.append('-')
#     else:
#         if not arr and chkarr:
#             if a > chkarr[-1]:
#                 for i in range(1,a+1):
#                     chkexist = chkarr.index(i) if i in chkarr else None
#                     if chkexist is None:
#                         arr.append(i)
#                         result.append('+')
#                         chkarr.append(i)
#                 arr.pop()
#         elif a < arr[-1]:
#             chkexist = chkarr.index(a) if a in chkarr else None
#             if chkexist is not None:
#                 while True:
#                     arr.pop()
#                     result.append('-')
#                     if not arr:
#                         print('NO')
#                         exit()
#                     elif arr[-1] == a:
#                         break
#                 arr.pop()
#                 result.append('-')
#         elif a > arr[-1]:
#             for i in range(arr[-1] + 1, a + 1):
#                 chkexist = chkarr.index(i) if i in chkarr else None
#                 if chkexist is None:
#                     arr.append(i)
#                     result.append('+')
#                     chkarr.append(i)
#                 elif chkexist is not None:
#                     chkexist = chkarr.index(a) if a in chkarr else None
#                     if chkexist is not None:
#                         print('NO')
#                         exit()
#             arr.pop()
#             result.append('-')
#         else:
#             arr.pop()
#             result.append('-')
# for i in result:
#     print(i)
#
#try1


a= int(input())
stack = []
r = []
c = 0

for i in range(a):
    inp = int(input())
    while c < inp:
        c += 1
        stack.append(c)
        r.append('+')
    if stack[-1] == inp:
        stack.pop()
        r.append('-')
    else:
        print('NO')
        exit()

for i in r:
    print(i)


#스택보다 작은값나오면 스택[-1]의 값이 그값이될때까지 빼는건줄알았는데
#그냥 그것까지 NO처리해야하는부분이였다...
#예제에서 3이 그냥 스택[-1]이 3이라 pop으로 튀어나온거였는데 그냥 이걸 빼면서도 갈수있다고 인식해버렸다.
