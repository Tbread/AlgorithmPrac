import math, sys, itertools

comb = itertools.combinations
sqrt = math.sqrt
primes = [1]
for i in range(2, 10000):
    flag = 0
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i)
rp = int(sys.stdin.readline())
for _ in range(rp):
    answers = []
    dif = []
    n = int(sys.stdin.readline())
    a, b = n // 2, n // 2
    while True:
        if a in primes and b in primes:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
