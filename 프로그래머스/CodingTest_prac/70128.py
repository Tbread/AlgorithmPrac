def solution(a, b):
    answer = 0
    for ae,be in zip(a,b):
        answer += ae * be
    return answer