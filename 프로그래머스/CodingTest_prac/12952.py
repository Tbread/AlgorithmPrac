def solution(n):
    board = [[0] * n for _ in range(n)]
    queens_location = []
    temp = []
    flag = 0
    for i in range(n):
        for j in range(n):
            for x in range(n):
                if board[x][j] == 1:
                    flag = 1
                    break
            if flag == 0:
                board[i][j] = 1
                temp.append([i, j])
            if flag == 0:
                flag = 0
                break
            flag = 0
    queens_location.append(temp)
    print(queens_location)
    for i in range(n):
        print(board[i])


solution(10)
