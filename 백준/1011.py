# import sys
#
# a = int(input())
# for repeat in range(a):
#     l = (sys.stdin.readline().strip()).split(' ')
#     goal = int(l[1]) - int(l[0])
#     speed = 1
#     remaindistance = goal
#     calc = 0
#     movedistance = 0
#     i = 0
#     chkd = 0
#     whentwice = 0
#     while(chkd < remaindistance):
#         i += 1
#         movedistance += speed
#         remaindistance = goal - movedistance
#         for m in range(1,speed+1):
#             calc += m
#         if remaindistance <= calc:
#             calc -= speed
#             whentwice = remaindistance - calc
#             speed -= 1
#             print(speed)
#         else:
#             speed += 1
#             print(speed)

# 복잡하게 머리속에서만 정리하지말고 생각나는대로 써서 코드로 풀어보자
# D가 출발지점부터 목표까지의 거리라고 했을때
# 1+2+3+.....n+n-1+n-2....3+2+1 의 값(N이라고 칭함) 이 D보다 항상 작거나 같아야한다
# 그럼 N값이 D를 초과하는순간의 지점을 찾아서 N값을 찾아내고
# 해당 N값에 사용됐던 n값으로 D - (n-1) = R이라고 했을때 R의 위치에서 한번 더 해당값을 늘리거나 줄이지않고 이동시키면된다
# 아니 쓰다보니 저 위를 구현시키는 코드를 작성하는게 아니라 그냥 N값을 적으면되는거같은데?

import sys
import math

root = math.sqrt
root2 = math.trunc

repeat = int(input())
for rp in range(repeat):
    xy = list(sys.stdin.readline().strip().split(' '))
    x = int(xy[0])
    y = int(xy[1])
    D = y - x
    # 고민을 해보자
    # y의값은 21억까지 들어올수있으니 for문을 돌리면 분명 시간초과가 걸릴것임
    # 만약 D의 값이 주어졌을때 n을 찾기위해 1부터 일일히 대입해볼게아니라 범위를 좁혀주는방법이 분명 있을것같음
    # 소수찾을때 sqrt사용하는것처럼
    # 50일때 -> 7 100일때 -> 10 134일때 ->11 378일때 ->19
    # 뭐야 진짜 그냥 제곱근인듯?
    n = root2(root(D))
    # N의 값은 등차수열항 n개*2-1(n값두번이니 한번빼줌)개로 만들어진다
    nsq = n ** 2
    ni = root(nsq)
    if D < 4:
        print(D)
    elif D > nsq + ni:
        print((2 * n) + 1)
    elif D > nsq and D <= ni + nsq:
        print(2 * n)
    elif D == nsq:
        print((2 * n) - 1)

    # 오늘의 교훈
    # 문제에서 말해주는 기능을 일일히 구현하지말고 그냥 그값을 도출해내는 식을 먼저 찾을수있을지 생각해보자...
    # 매우큰 꺠달음이였다
