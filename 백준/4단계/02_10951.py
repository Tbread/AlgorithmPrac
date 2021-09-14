while True:
    try:
        userinput = input().split(' ')
        a = int(userinput[0])
        b = int(userinput[1])
        print(a+b)
    except EOFError:
        break