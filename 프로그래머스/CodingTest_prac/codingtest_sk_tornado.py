def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    inc_num = 1
    mv = 0
    if clockwise is True:
        moves = [[[0, 1], [1, 0], [-1, 0], [0, -1]], [[1, 0], [0, -1], [0, 1], [-1, 0]],
                 [[0, -1], [-1, 0], [1, 0], [0, 1]], [[-1, 0], [0, 1], [0, -1], [1, 0]]]
        move = moves[mv]
    else:
        moves = [[[1, 0], [0, -1], [0, 1], [-1, 0]], [[0, 1], [1, 0], [-1, 0], [0, -1]],
                [[-1, 0], [0, 1], [0, -1], [1, 0]], [[0, -1], [-1, 0], [1, 0], [0, 1]]]
        move = moves[mv]
    coords = [[0, 0], [0, n - 1], [n - 1, 0], [n - 1, n - 1]]
    even = 1
    while True:
        for i in range(n - even):
            for coord in coords:
                answer[coord[0]][coord[1]] = inc_num
            inc_num += 1
            for m in range(4):
                for j in range(2):
                    coords[m][j] = coords[m][j] + move[m][j]
        even += 2
        for m in range(4):
            for j in range(2):
                coords[m][j] = coords[m][j] - move[m][j]
        mv += 1
        if mv == 4:
            mv = 0
        move = moves[mv]
        for m in range(4):
            for j in range(2):
                coords[m][j] = coords[m][j] + move[m][j]
        if n - even < 1:
            break
    if n % 2 == 1:
        mid = int(n / 2)
        answer[mid][mid] = inc_num
    return answer

arr = solution(5,True)
for i in arr:
    print(i)