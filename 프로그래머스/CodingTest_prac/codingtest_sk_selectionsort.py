def solution(p):
    change_log = []
    for i in range(len(p)):
        change_log.append(0)
    for i in range(len(p)-1):
        idx = i
        init_idx = i
        for j in range(i+1,len(p)):
            if p[j] < p[idx]:
                idx = j
        if not idx == init_idx:
            p[i],p[idx] = p[idx],p[i]
            change_log[i] += 1
            change_log[idx] += 1
    return change_log


solution([2, 5, 3, 1, 4])
