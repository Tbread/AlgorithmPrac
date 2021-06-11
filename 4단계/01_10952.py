while True:
    userinput = input().split(' ')
    a = int(userinput[0])
    b = int(userinput[1])
    if a == 0 and b == 0:
        break
    else:
        print(a+b)