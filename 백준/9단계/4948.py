# while True:
#     N = int(input())
#     if N == 0:
#         break
#     ea = 0
#     for i in range(N + 1, (2 * N) + 1):
#         flag = 0
#         for m in range(2, i):
#             if i % m == 0:
#                 flag = 1
#                 break
#         if flag != 1:
#             ea += 1
#     print(ea)
#
# try1

# n = 100
# arr = []
# for i in range(1, n):
#     flag = 0
#     if i == 1:
#         arr.append(0)
#         pass
#     else:
#         for v in range(2, i+1):
#             if i % n == 0:
#                 flag = 1
#                 break
#         if flag == 0:
#             arr.append(1)
#         else:
#             arr.append(0)
# print(arr)
#
# try2
#
# import math
#
# arr = [0, 0]
# N = 123456 * 2
# R = int(math.sqrt(N))
# ea = 0
# for i in range(N + 1, (2 * N) + 1):
#     flag = 0
#     for m in range(2, R):
#         if i % m == 0:
#             flag = 1
#             break
#     if flag != 1:
#         arr.append(1)
#     else:
#         arr.append(0)
#
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     for i in range(a + 1, (a * 2) + 1):
#         ea += arr[i]
#     print(ea)
#
#try3

import math
sqrt = math.sqrt
N = 123456*2+1
arr = [1]*N
for i in range(1,N):
    if i == 1:
        pass
    for v in range(2,int(sqrt(i))+1):
        if i%v == 0:
            arr[i] =0
            break

while True:
    a = int(input())
    ea = 0
    if a == 0:
        break
    for i in range(a+1,a*2+1):
        ea += arr[i]
    print(ea)

#

prime_list = []
for n in range(2, 123456 * 2 + 1):
    for i in prime_list:
        if n % i == 0 and i * i <= n:
            break
    else:
        prime_list.append(n)
while 1:
    nums = int(input())
    if nums == 0:
        break
    else:
        counts = 0
        for i in range(nums + 1, 2 * nums + 1):
            if i in prime_list:
                counts += 1
        print(counts)