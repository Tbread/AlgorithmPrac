# import heapq
#
# push = heapq.heappush
# pop = heapq.heappop
#
#
# def solution(N, coffee_times):
#     answer = []
#     heap = []
#     passedTime = [0]
#     times = 0
#     for i in range(len(coffee_times) + N):
#         if i < len(coffee_times):
#             push(heap, coffee_times[i]+passedTime[times])
#         if len(heap) == N:
#             popNum = pop(heap)
#             passedTime.append(popNum)
#             temp = coffee_times[:i+1]
#             idx = temp.index(popNum-passedTime[times])
#             answer.append(idx + 1)
#             coffee_times[idx] = 0
#             print(coffee_times)
#             times += 1
#     print(answer)
#     return answer

def solution(N, coffee_times):
    answer = []
    num = N + 2
    while True:
        arr = coffee_times[:N + 1]
        for i in range(len(arr)):
            arr[i] -= 1
        try:
            answer.append(arr.index(0))
            arr.append(coffee_times[num])
            num += 1
        except:
            pass
        for i in range(len(arr)):
            if arr[i] > 0:
                continue
            flag
        if flag =

solution(3, [4, 2, 2, 5, 3])
