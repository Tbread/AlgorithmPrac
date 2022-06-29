def solution(n, times):
    answer = float("inf")
    min = 0
    max = sorted(times)[-1] * n
    while (min <= max):
        mid = (min + max) // 2
        cnt = 0
        for i in times:
            cnt += mid // i
        if cnt < n:
            min = mid + 1
        else:
            if mid < answer:
                answer = mid
            max = mid - 1
    return answer



solution(6, [7, 10])
