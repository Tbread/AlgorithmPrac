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


import math
sqrt = math.sqrt
n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    D = sqrt((x1-x2)**2 + (y1-y2)**2)
    #피타고라스의정리로 거리를 구했음
    if D == 0 and r1 == r2 :
        # 두점이 겹쳐있다는 뜻
        print(-1)
    elif abs(r1-r2) == D or r1 + r2 == D:
        #두점의 거리가 r1+r2와 같다면 가능한 위치는 하나이고 해당점을 기점으로 r1,r2를 반지름으로 하는 원을 그렸을때 외접함
        #위처럼 원을 그렸을때 큰원의 반지름에서 두점 사이의 거리를 뺐을때 작은원의 반지름이 나온다면 내접하는 원임(가능한곳은 한개)
        print(1)
    elif abs(r1-r2) < D < (r1+r2) :
        #큰원반지름-작은원반지름 했는데 두점사이의 거리보단 작고 두점에서 목표위치까지의 거리를 합친것보다 작다면 두곳이가능함(벤다이어그램마냥 원이겹침)
        print(2)
    else:
        print(0)
        #ㅁㄹ 안만나나봄
