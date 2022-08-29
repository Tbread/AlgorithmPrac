def solution(n):
    n = list(str(n))
    answer = []
    while n:
        answer.append(int(n.pop()))
    return answer