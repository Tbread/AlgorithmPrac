def solution(lottos, win_nums):
    answer = []
    win = 0
    unknown = 0
    high = 0
    low = 0
    for i in lottos:
        if not i == 0:
            for j in win_nums:
                if i == j:
                    win += 1
        elif i == 0:
            unknown += 1
    max = win + unknown
    high = 7 - max
    low = 7 - win
    if low == 7:
        low = 6
    if high == 7:
        high = 6
    answer.append(high)
    answer.append(low)
    return answer