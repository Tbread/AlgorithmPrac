import math

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        temp = []
        dnums = []
        for j in range(1,int(math.sqrt(i)+1)):
            if i % j == 0:
                temp.append(j)
        for dnum in temp:
            dnums.append(dnum)
            dnums.append(i//dnum)
        dnums = list(set(dnums))
        if len(dnums) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer