import math
from queue import Queue
from math import ceil
ceil = math.ceil

def solution(progresses, speeds):
    que = Queue()
    answer = []
    length = len(progresses)
    for progress,speed in zip(progresses,speeds):
        que.put([progress,speed])
    days_gone = 0
    idx = -1
    while not que.empty():
        progress,speed = que.get()
        days = ceil((100 - progress) / speed)
        if days > days_gone:
            answer.append(1)
            idx += 1
            days_gone = days
        else:
            answer[idx] += 1
    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
