
repeat = int(input())

for rp in range(repeat):
    a = input()
    while True:
        a = a.replace('()','')
        try:
            emptychk = a.index('()')
        except ValueError:
            break
    if a == '':
        print('YES')
    else:
        print('NO')