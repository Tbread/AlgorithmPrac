import itertools,math
root = math.sqrt
comb = itertools.combinations
def solution(numbers):
    numbers = list(map(int,list(numbers)))
    ea = len(numbers)
    combs = []
    if ea == 1:
        if numbers[0] == 2 or numbers[0] == 3 or numbers[0] == 1:
            return 1
        for i in range(2,int(root(numbers[0]))):
            if root % i == 0:
                return 0
        return 1
    for i in range(ea,1,-1):
        combs.append(comb(numbers),ea)
    print(combs)

solution("017")