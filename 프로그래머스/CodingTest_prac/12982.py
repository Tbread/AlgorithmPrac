import heapq

def solution(d, budget):
    heapq.heapify(d)
    answer = 0
    while budget >= 0:
        if d:
            budget -= heapq.heappop(d)
        else:
            answer += 1
            break
        answer += 1

    return answer - 1

solution([1,3,2,5,4],9)