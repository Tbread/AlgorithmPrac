a = int(input())
if a == 1:
    print('1/1')
else:
    b = 0
    i = 0
    x = 0
    y = 0
    while (b < a):
        i += 1
        b += i
    for m in range(i):
        a -= m

    if i % 2 == 0:
        x = i - a + 1
        y = a
    else:
        x = a
        y = i - a + 1
    print(str(y)+'/'+str(x))

