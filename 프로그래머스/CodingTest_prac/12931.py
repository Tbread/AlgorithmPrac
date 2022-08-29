def solution(n):
    n = list(str(n))
    answer = 0
    for num in n:
        answer += int(num)
    return answer
