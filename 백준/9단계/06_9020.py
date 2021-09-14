import math

sqrt = math.sqrt
arr = []


def chk(get):
    if get == 1:
        return False
    for i in range(2, int(sqrt(get)) + 1):
        if get % i == 0:
            return False
    return True


def filt(get):
    global n
    if get < n//2:
        return True
    else:
        return False


for i in range(2, 10000):
    if chk(i) == True:
        arr.append(i)

repeat = int(input())
for _ in range(repeat):
    n = int(input())
    arr2 = list(filter(filt, arr))
    li = []
    for i in range(len(arr2)-1, -1, -1):
        for j in range(len(arr2)-1,-1,-1):
            if arr2[i]+arr2[j] == n:
                li2 = []
                li2.append(arr2[i])
                li2.append(arr2[j])
                li.append(li2)
        if i < len(arr2)/2:
            break
    past_dif = abs(li[0][0] - li[0][1])
    for i in range(len(li)):
        dif = abs(li[i][0]-li[i][1])
        if dif <= past_dif:
            c = i
            past_dif = dif
    print(*li[c])