import heapq

pop = heapq.heappop
push = heapq.heappush

def solution(X, Y):
    X, Y = list(X), list(Y)
    common = []

    for element in Y:
        if element in X:
            X.remove(element)
            push(common,int(element))
    if not common:
        return "-1"
    zeroTest = set(common)
    try:
        zeroTest.remove(0)
    except:
        pass
    if not zeroTest:
        return "0"
    temp = ""
    for i in range(len(common)):
        temp += str(pop(common))
    return temp[::-1]