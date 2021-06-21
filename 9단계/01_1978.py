import math
sqrt = math.sqrt

def chk(get):
    if get == 1:
        return False
    for i in range(2,int(sqrt(get))+1):
        if get%i == 0:
            return False
    return True

n = int(input())
l = list(map(int,input().split()))
c = 0
for i in range(n):
    if chk(l[i]) == True:
        c += 1
print(c)