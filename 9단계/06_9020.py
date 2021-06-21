import math
sqrt = math.sqrt
arr = []
def chk(get):
    if get == 1:
        return False
    for i in range(2,int(sqrt(get))+1):
        if get%i == 0:
            return False
    return True

def filt(get):
    global n
    if get < n:
        return True
    else:
        return False

for i in range(2,10000):
    if chk(i) == True:
        arr.append(i)

repeat = int(input())
for _ in range(repeat):
    n = int(input())
    arr2 = list(filter(filt,arr))
    li = []
    flag = 0
    for i in range(len(arr2)//2,-1,-1):
        chk2 = n - arr2[i]
        if chk(chk2) == True:
            li.append(arr2[i])
            li.append(chk2)
            li.sort()
            print(*li)
            break