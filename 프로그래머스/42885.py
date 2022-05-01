import itertools
from collections import deque

def solution(people, limit):
    head = len(people)
    if head == 1:
        return 1
    combs = deque()
    possibles = []
    for i in range(1,head+1):
        combs += list(itertools.combinations(people,i))
    for i in range(len(combs)):
        combs[i] = list(combs[i])
    possibles.append(combs.pop())
    for i in range(len(combs)//2):
        first = combs.popleft()
        sec = combs.pop()
        possibles.append([first,sec])
    print(possibles)


solution([1,2,3,4,5,6,7],100)