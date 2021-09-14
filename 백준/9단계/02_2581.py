import math
sqrt = math.sqrt

def chk(get):
    if get == 1:
        return False
    for i in range(2,int(sqrt(get))+1):
        if get%i == 0:
            return False
    return True

M = int(input())
N = int(input())
c = 0
sum = 0
chkt = 0
for i in range(M,N+1):
    if chk(i) == True:
        c += 1
        sum += i
        if chkt == 0:
            smallest = i
            chkt = 1
if c == 0:
    print('-1')
else:
    print(sum)
    print(smallest)
