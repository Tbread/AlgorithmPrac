# # # 위치들을 변수에넣고 그냥 돌릴때마다 해당위치같이 + -해주고 계속 0기준 검색하면될듯
# # # 돌리는방법: 걍 arr.append(arr[0])하고 pop하면될거같음 역방향이면 -1 append하고 rightpop인가 popright인가 그거쓰고
# # # 근데 생각해보니 식으로 풀릴수도있을거같으니 생각부터해보자
# # # 배열의크기가 N이라할때 뽑을수의위치 P가 N/2보다 크면 역방향으로 땡겨오고 작으면 정방향으로 읽으면됨
# # import sys
# #
# # nm = list(sys.stdin.readline().strip().split(' '))
# # N = int(nm[0])
# # M = int(nm[1])
# # P = list(map(int, input().split()))
# # C = 0
# #
# # for i in range(M):
# #     if P[i] <= (N / 2):
# #         C = C + (P[i] - 1)
# #         X = P[i] - 1
# #         for j in range(M):
# #             if i == j:
# #                 pass
# #             elif P[j] < P[i]:
# #                 P[j] += X
# #             else:
# #                 P[j] -= P[i]
# #             P[j] = P[j] - X - 1
# #     else:
# #         C = C + (N - P[i] + 1)
# #         X = N - P[i] + 1
# #         for j in range(M):
# #             if i == j:
# #                 pass
# #             elif P[j] < P[i]:
# #                 P[j] += X
# #             else:
# #                 P[j] -= P[i]
# #     N = N - 1
# # print(C)
#
import sys
from collections import deque

nm = list(sys.stdin.readline().strip().split(' '))
N = int(nm[0])
M = int(nm[1])
P = list(map(int, sys.stdin.readline().split()))
C = 0
Q = deque(range(1, N + 1))

for i in range(len(P)):
    if P[i] == Q[0]:
        Q.popleft()
        continue
    findthis = Q.index(P[i])

    if findthis > len(Q)/2:
        Q.rotate(len(Q) - findthis)
        C += (len(Q) - findthis)

    elif findthis <= len(Q)/2:
        Q.rotate(-findthis)
        C += findthis
    Q.popleft()

print(C)
