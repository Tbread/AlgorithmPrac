def solution(board, moves):
    mx = len(board[0])
    stack = []
    answer = 0
    for move in moves:
        move -= 1
        for i in range(mx):
            if len(stack) == 0 and board[i][move] != 0:
                stack.append(board[i][move])
                board[i][move] = 0
                break
            elif board[i][move] != 0:
                if stack[-1] == board[i][move]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move])
                board[i][move] = 0
                break

    return answer
