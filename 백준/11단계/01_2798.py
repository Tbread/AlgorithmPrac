import sys
from itertools import combinations

# arr = [1,2,3,4,5]
# a = list(combinations(arr,3))
# print(a)
# #[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)] 반환


nm = (sys.stdin.readline().strip()).split(' ')
n = int(nm[0])
m = int(nm[1])
past_sum = 0

inp = list(combinations(sys.stdin.readline().split(), 3))
sumarr = []
for i in range(len(inp)):
    sum = int(inp[i][0]) + int(inp[i][1]) + int(inp[i][2])
    if sum == m:
        past_sum = sum
        break
    elif sum > m:
        pass
    elif sum < m and sum > past_sum:
        past_sum = sum
    elif sum < past_sum:
        pass
print(past_sum)
# count = 0
# arr = []
# inp = (sys.stdin.readline().strip()).split(' ')
# for i in range(n):
#     arr.append(int(inp[i]))
# past_sum = 0
# sum = 0
# for i in range(n - 2):
#     for j in range(1, n - 1):
#         if count == n:
#             count = 0
#         for k in range(2, n):
#             k = int(k + (count / (n - 2)))
#             print(i, j, k)
#             count += 1
#             #             sum = arr[i] + arr[j] + arr[k]
#             #             if sum == m:
#             #                 print(sum)
#             #                 exit()
#             #             elif sum > past_sum and sum < m:
#             #                 past_sum = sum
#             #             elif sum < past_sum:
#             #                 pass
#             #             elif sum > m:
#             #                 pass
#             # print(past_sum)
