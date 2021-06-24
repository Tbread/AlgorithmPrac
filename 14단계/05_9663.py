def chkchessboard(ans, n):
    global c
    if len(ans) == n:
        c += 1
        return 0
    chessboard = list(range(n))
    for i in range(len(ans)):
        if ans[i] in chessboard:
            chessboard.remove(ans[i])
        d = len(ans) - i
        if ans[i] + d in chessboard:
            chessboard.remove(ans[i] + d)
        if ans[i] - d in chessboard:
            chessboard.remove(ans[i] + d)
    if chessboard:
        for i in chessboard:
            ans.append(i)
            chkchessboard(ans, n)
    else:
        return 0


c = 0
num = int(input())
for i in range(num):
    chkchessboard([i], num)
print(count)
