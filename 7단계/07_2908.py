a = input().split(' ')
b = ''.join(list(reversed(list(a[0]))))
c = ''.join(list(reversed(list(a[1]))))

if b < c:
    print(c)
else:
    print(b)