from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    sum1 = sum(queue1)
    queue2 = deque(queue2)
    sum2 = sum(queue2)

    for i in range(len(queue1)*3+1):
        if sum1 == sum2:
            return i
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
    return -1
