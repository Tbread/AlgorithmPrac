inp = list(map(int, input().split()))

a1 = inp[2] - inp[0]
b1 = inp[3] - inp[1]
a2 = inp[0]
b2 = inp[1]

if a1 < a2:
    a = a1
else:
    a = a2
if b1 < b2:
    b = b1
else:
    b = b2
if a < b:
    print(a)
else:
    print(b)
