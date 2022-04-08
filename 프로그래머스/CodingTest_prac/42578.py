# import itertools
#
#
# def solution(clothes):
#     answer = 0
#     clothes_dict = {}
#     for cloth in clothes:
#         if cloth[1] in clothes_dict:
#             clothes_dict[cloth[1]] += 1
#         else:
#             clothes_dict[cloth[1]] = 1
#     arr = []
#     for key, value in clothes_dict.items():
#         arr.append(key)
#     combines = []
#     for i in range(1, len(arr) + 1):
#         combines.append(list(itertools.combinations(arr, i)))
#     for i in range(len(combines)):
#         for j in range(len(combines[i])):
#             combines[i][j] = list(combines[i][j])
#     for i in range(len(combines)):
#         for j in range(len(combines[i])):
#             if len(combines[i][j]) == 1:
#                 for m in range(len(combines[i][j])):
#                     answer += clothes_dict[combines[i][j][m]]
#             else:
#                 temp = 1
#                 for m in range(len(combines[i][j])):
#                     temp *= clothes_dict[combines[i][j][m]]
#                 answer += temp
#     return answer

# 시간초과

import itertools


def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    arr = []
    for key, value in clothes_dict.items():
        arr.append(value)
    for i in arr:
        answer *= i+1
    return answer - 1

