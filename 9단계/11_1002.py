# #좌표거리구하는법
# # x1 != x2 and y1 != y2 일때 피타고라스의 x3 = x1 x2중큰수 y3 = y1 y2중 아무거나 하고 피타고라스의 정리 이용하면됨
# #절대값(주어진 x1 - 구할값 n(=x3))^2+주어진y1^2=거리^2 즉
# #절대값(주어진 x1 - 구할값 n(=x3)=sqrt(거리^2-y^2)
# #절대값(주어진 x1 - 구할값 n(=x3)=sqrt(거리^2-y^2)
# import math
# import sys
# root = math.sqrt
#
# repeat = int(input())
#
# for rp in range(repeat):
#     inp = list(map(int, sys.stdin.readline().split()))
#     x1 = inp[0]
#     y1 = inp[1]
#     r1 = inp[2]
#     x2 = inp[3]
#     y2 = inp[4]
#     r2 = inp[5]
#
# 쓰다보니 이렇게하는게 아닌거같음
