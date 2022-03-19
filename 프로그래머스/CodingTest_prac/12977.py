import itertools,math
comb = itertools.combinations
root = math.sqrt
def solution(nums):
    answer = 0
    sums = []
    combs = list(comb(nums,3))
    for combine in combs:
        sums.append(sum(combine))
    for num in sums:
        flag = 0
        if num % 2 == 0:
            continue
        else:
            for i in range(2,int(root(num))+1):
                if num % i == 0:
                    flag = 1
                    break
            if flag != 1:
                answer += 1
    return answer