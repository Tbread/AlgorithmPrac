def solution(n):
    if n == 1:
        return 1
    if n > 15:
        return 0
    leaves = 14
    answer = 1
    for i in range(n-1):
        answer = answer * (leaves / 54)
    answer *= 100
    answer = str(answer) + '%'
    return answer

