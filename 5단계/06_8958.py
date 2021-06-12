# import sys
# a = int(input())
# scores = []
# for tot in range(a):
#     l = (sys.stdin.readline().strip())
#     sw = len(l)
#     s = 1
#     ox = list(l)
#     arr = []
#     score = 0
#     for i in range(1,sw):
#         if ox[i-1] == ox[i] and i != sw-1:
#             s += 1
#         elif i == sw-1:
#             if ox[i] == ox[i-1]:
#                 s+=1
#                 if ox[i] != 'X':
#                     arr.append(s)
#             else:
#                 if ox[i] != 'X':
#                     s = 1
#                     arr.append(s)
#                 else:
#                     arr.append(s)
#         else:
#             if ox[i] != 'O':
#                 arr.append(s)
#             s = 1
#
#     for i in range(len(arr)):
#         for v in range(arr[i]+1):
#             score += v
#     scores.append(score)
#
# for i in range(a):
#     print(scores[i])

a = int(input())

for i in range(a):
    b = input()
    score = 0
    sum = 0
    for m in b:
        if m == 'O' or m == 'o':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
