from itertools import combinations
import heapq

def solution(numbers):
    comb = list(combinations(numbers,2))
    temp = []
    answer = []
    for i in comb:
        temp.append(sum(i))
    temp = list(set(temp))
    heapq.heapify(temp)
    for i in range(len(temp)):
        answer.append(heapq.heappop(temp))
    return answer



solution([2,1,3,4,1])