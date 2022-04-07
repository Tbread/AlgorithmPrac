from collections import deque
import sys


def solution(priorities, location):
    deq = deque()
    answer = 0
    for i in range(len(priorities)):
        deq.append([priorities[i], i])
    while True:
        deq, removed_location = remove_highest(deq)
        answer += 1
        if removed_location == location:
            return answer


def remove_highest(deq):
    length = len(deq)
    prior = 0
    idx = -1
    highest_idx = -1
    for _ in range(length):
        idx += 1
        temp = deq.popleft()
        if temp[0] > prior:
            prior = temp[0]
            highest_idx = idx
        deq.append(temp)
    deq.rotate(-highest_idx)
    highest = deq.popleft()
    return deq, highest[1]


repeat = int(sys.stdin.readline())
for _ in range(repeat):
    answer = 0
    deq = deque()
    counts, location = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(arr,location))