import itertools,math
root = math.sqrt
def solution(numbers):
    numbers = list(map(int,list(numbers)))
    ea = len(numbers)
    perms = []
    for i in range(1,ea+1):
        perms += list(itertools.permutations(numbers,i))
    combs = []
    answer = 0
    for i in range(len(perms)):
        temp = ''
        for j in range(len(perms[i])):
            temp += str(perms[i][j])
        combs.append(int(temp))
    combs = list(set(combs))
    for i in range(len(combs)):
        flag = 0
        if combs[i] <= 1:
            continue
        if combs[i] == 2:
            answer += 1
            continue
        if combs[i] % 2 == 0:
            continue
        for j in range(2,int(root(combs[i]))+1):
            if combs[i] % j == 0:
                flag = 1
                break
        if flag == 0:
            answer +=1
    return answer
solution("1231")