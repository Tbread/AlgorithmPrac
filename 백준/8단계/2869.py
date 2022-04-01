# inp = input().split()
# a = int(inp[0])
# b = int(inp[1])
# c = int(inp[2])
# if a > c:
#     print('1')
# elif:
#     b > a and c > a:
# else:
#     num1 = c / (a - b)
#     num2 = num1 - 1
#     if num2 * (a - b) < c and num2 * (a - b) + a >= c:
#         num1 -= 1
#         if num1 < 1:
#             num1 = 1
#     print(int(num1))

# 얘도 기능구현을 하려하지말고 계산을 해보자고
# 만약 하루에 가는높이 A가 V보다 크거나같으면 1이고 B를 볼필요가없음
# 첫날낮 이동거리 A를 V에서 빼주고 (낮에 도착했는데 밤에 미끄러지면안되니까...)하루이동거리 그러니까 A-B를 나눠주면 앵간하면나온다

import sys

inp = (sys.stdin.readline().strip()).split(' ')
a = int(inp[0])
b = int(inp[1])
v = int(inp[2])

if a >= v:
    print('1')
elif (v - a) % (a - b) != 0:
    print(int((v - a) / (a - b) + 2)) #내일낮에A만큼더가야하니까 기본+1에 +1해서 +2
else:
    print(int((v - a) / (a - b) + 1)) #낮만큼 이미간걸 계산해놨으니 기본+1

#이건 전의내가 멍청했던건가 내가 성장을한건가