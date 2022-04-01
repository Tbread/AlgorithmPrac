import sys
t = int(sys.stdin.readline())
for i in range(t):
    temp = 1
    m = int(sys.stdin.readline()) + 1
    n = int(sys.stdin.readline())
    rooms = [[0] * n for _ in range(m)]
    for i in range(n):
        rooms[0][i] = i+1
    for i in range(m):
        rooms[i][0] = 1
    for i in range(1,m):
        for j in range(1,n):
            if j == 1:
                temp = 1
            temp += rooms[i-1][j]
            rooms[i][j] = temp
    print(rooms[-1][-1])