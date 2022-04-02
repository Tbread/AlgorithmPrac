import sys

sys.setrecursionlimit(10**6)

def find(arr, sx, sy, num, x, y, check):
    coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if arr[sx][sy] == 0:
        return arr, num, check
    arr[sx][sy] = 0
    num += 1
    for coord in coords:
        if (0 <= sx + coord[0] < x) and (0 <= sy + coord[1] < y):
            if [sx + coord[0], sy + coord[1]] in check:
                continue
            check.append([sx + coord[0], sy + coord[1]])
            if arr[sx+coord[0]][sy+coord[1]] == 0:
                continue
            arr, num, check = find(arr, sx + coord[0], sy + coord[1], num, x, y, check)
    return arr, num, check



repeat = int(sys.stdin.readline().strip())
for _ in range(repeat):
    result = []
    check = []
    x, y, n = map(int, sys.stdin.readline().split())
    map_arr = [[0] * y for _ in range(x)]
    for _ in range(n):
        bx, by = map(int, sys.stdin.readline().split())
        map_arr[bx][by] = 1
    for i in range(y):
        for j in range(x):
            if [j,i] in check:
                continue
            check.append([j,i])
            if map_arr[j][i] == 0:
                continue
            map_arr, num, check = find(map_arr, j, i, 0, x, y, check)
            if num != 0:
                result.append(num)
    print(len(result))
