import heapq
h = heapq
hpop = h.heappop
def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        if scoville[0] >= K:
            return answer
        temp1 = hpop(scoville)
        temp2 = hpop(scoville)
        ele = temp1 + (temp2 * 2)
        h.heappush(scoville,ele)
        answer += 1