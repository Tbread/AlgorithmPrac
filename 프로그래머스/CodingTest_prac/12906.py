def solution(arr):
    answer = []
    temp = 1000001
    for i in arr:
        if temp == i:
            continue
        answer.append(i)
        temp = i
    return answer

solution([1,1,3,3,0,1,1])