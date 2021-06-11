a = int(input())
str = ''
str2 = ''

for i in range(a + 1):
    for v in range(i):
        str += '*'
    if str == '':
        continue
    for e in range((a + 1) - v):
        if e <= 1:
            pass
        else:
            str2 += ' '
    else:
        print(str2 + str)
    str = ''
    str2 = ''
