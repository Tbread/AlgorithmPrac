a = int(input())
b = int(input())
if a > 0:
    c1 = 0
else:
    c1 = 1
if b > 0:
    c2 = 0
else:
    c2 = 1

if c1 == 0 and c2 == 0:
    print('1')
elif c1 == 1 and c2 == 0:
    print('2')
elif c1 == 1 and c2 == 1:
    print('3')
else:
    print('4')
