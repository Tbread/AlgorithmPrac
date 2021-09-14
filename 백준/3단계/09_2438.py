a = int(input())
str = ''

for i in range(a+1):
    for v in range(i):
        str += '*'
    if str == '':
        continue
    else:
        print(str)
    str = ''