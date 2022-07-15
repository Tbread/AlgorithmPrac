def solution(n, horizontal):
    rooms = [[0] * n for i in range(n)]
    flag = 1
    count = 0
    turn = 0
    now = [0, 0]
    move = [0, 0]
    if horizontal:
        move = [0, -1]
    else:
        move = [-1, 0]
    while count == n:
        for i in range(flag):
            rooms[now[0]][now[1]] = turn
        if now[0] + move[0] >= n or now[0] + move[0] < 0 or now[1] + move[1] >= n or now[1] + move[1] < 0:
            if horizontal:
                horizontal = False
            if not horizontal:
                horizontal = True
#
#
# print(solution(5, True))
