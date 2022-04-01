import math
sqrt = math.sqrt

def chk(get):
    if get == 1:
        return False
    for i in range(2,int(sqrt(get))+1):
        if get%i == 0:
            return False
    return True

N = int(input())
dv = 2
if N == 1:
    exit()
if chk(N) == True:
    print(N)
    exit()
while True:
    if N%dv == 0:
        print(dv)
        N = N//dv
    else:
        dv += 1
    if chk(N) == True:
        print(N)
        break
