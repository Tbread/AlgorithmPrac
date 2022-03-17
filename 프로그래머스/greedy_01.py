def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    losts = []
    for lo in lost:
        losts.append(lo)
    for borrow in lost:
        if borrow - 1 in reserve:
            idx = losts.index(borrow)
            losts.pop(idx)
            idx = reserve.index(borrow - 1)
            reserve.pop(idx)
            continue
        if borrow in reserve:
            idx = losts.index(borrow)
            losts.pop(idx)
            idx = reserve.index(borrow)
            reserve.pop(idx)
            continue
        if borrow + 1 in reserve:
            idx = losts.index(borrow)
            losts.pop(idx)
            idx = reserve.index(borrow + 1)
            reserve.pop(idx)
    return n - len(losts)


print(solution(5, [2, 3, 4], [3,4,5]))

#테스트케이스5번 실패