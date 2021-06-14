import sys
l = sys.stdin.readline().strip().split(' ')
a = int(l[0])
b = int(l[1])
aarr = []
barr = []
if a % b == 0:
    max_common_divisor = b
    least_common_multiple = a

elif b % a == 0:
    max_common_divisor = a
    least_common_multiple = b
else:
    for i in range(2, a):
        if a % i == 0:
            temp = int(a / i)
            aarr.append(temp)
    for i in range(2, b):
        if b % i == 0:
            temp = int(b / i)
            barr.append(temp)

    common_divisor = list(set(aarr) & set(barr))
    common_divisor.sort()
    if common_divisor == []:
        max_common_divisor = 1
        least_common_multiple = a * b
    else:
        max_common_divisor = common_divisor[-1]
        ad = int(a / max_common_divisor)
        bd = int(b / max_common_divisor)
        least_common_multiple = ad * bd * max_common_divisor


print(max_common_divisor)
print(least_common_multiple)
