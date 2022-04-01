N =int(input())


c = 0
while True:
    if N == 1:
        print(c)
        exit()
    if N % 3 == 0:
        N = N//3
        c += 1
    elif N % 3 == 1:
        N = N - 1
        c += 1
    elif N % 2 == 0:
        N = N//2
        c += 1
    else:
        N = N -1
        c += 1

#실패
