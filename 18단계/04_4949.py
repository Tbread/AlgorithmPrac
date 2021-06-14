while True:
    string = input()
    if string == '.':
        break
    ls = list(string)
    sl = list(reversed(ls))
    new_str = ls
    new_trs = sl

    # b위치 = -(b+1)
    while True:
        try:
            a = new_str.index('(')
        except ValueError:
            flag = 1
            pass
        try:
            b = new_trs.index(')')
        except ValueError:
            if flag == 1:
                break
            else:
                fail = 1
                break
        new_str = []
        for i in range(a + 1, len(ls) - b):
            new_str.append(ls[i])
    if fail == 1:
        print('no')
        break
    print(new_str)
