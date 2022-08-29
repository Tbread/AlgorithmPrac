from math import sqrt

def solution(n):
    if sqrt(n) == int(sqrt(n)):
        return (int(sqrt(n))+1)**2
    else:
        return -1

solution(3)