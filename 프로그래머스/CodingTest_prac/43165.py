import copy


def deep(abss, n, numlen):
    newarr = []
    for abs in abss:
        temp1 = copy.deepcopy(abs)
        temp2 = copy.deepcopy(abs)
        temp1[n] = '-'
        temp2[n] = '+'
        newarr.append(temp1)
        newarr.append(temp2)
    if n == numlen - 1:
        return newarr
    else:
        return deep(newarr,n+1,numlen)



def solution(numbers, target):
    abss = [[0] * len(numbers)]
    abss = deep(abss, 0, len(numbers))
    answer = 0
    for abs in abss:
        temp = ''
        for i in range(len(numbers)):
            temp += abs[i]
            temp += str(numbers[i])
        if eval(temp) == target:
            answer += 1
    return answer


solution([1, 1, 1, 1, 1], 3)
