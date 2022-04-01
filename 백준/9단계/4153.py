while True:
    inp = list(map(int,input().split()))
    inp.sort()
    if sum(inp) == 0:
        exit()
    if inp[0]**2 + inp[1]**2 == inp[2]**2:
        print('right')
    else:
        print('wrong')