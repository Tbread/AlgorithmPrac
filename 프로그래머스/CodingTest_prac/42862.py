def solution(n, lost, reserve):
    afterlost = list(set(lost) - set(reserve))
    afterreserve = list(set(reserve) - set(lost))
    lost = afterlost
    reserve = afterreserve
    res_dict = {}
    lostp = len(lost)
    for i in reserve:
        res_dict[i] = 1
    for i in lost:
        if i-1 in res_dict and res_dict[i - 1] == 1:
            res_dict[i - 1] = 0
            lostp -= 1
        elif i+1 in res_dict and res_dict[i + 1] == 1:
            res_dict[i + 1] = 0
            lostp -= 1
    return n - lostp

solution(5, [2, 4], [3])