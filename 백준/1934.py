import sys
repeat = int(input())
for rp in range(repeat):
    l = sys.stdin.readline().strip().split(' ')
    a = int(l[0])
    statica = a
    b = int(l[1])
    staticb = b
    if a % b == 0:
        max_common_divisor = b
        least_common_multiple = a

    elif b % a == 0:
        max_common_divisor = a
        least_common_multiple = b
    else:
        if a<b:
            tempa = b
            tempb = a
            a = tempa
            b = tempb
        while True:
            least = a % b
            if least == 0:
                max_common_divisor = b
                break
            else:
                a = b
                b = least
    least_common_multiple = max_common_divisor * int(staticb/max_common_divisor) * int(statica/max_common_divisor)
    print(least_common_multiple)