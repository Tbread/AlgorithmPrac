import math

sqrt = math.sqrt
pn = [1, 2, 3]
for i in range(5, 9876544):
    temp_num = int(sqrt(i))
    for j in range(1,temp_num):
        if temp_num % j == 0:
            break
        pn.append(pn)
    print(i)
for i in pn:
    pn_num = list(str(i))
    temp_list = set(pn_num)
    if len(pn_num) != len(temp_list):
        pn.remove(i)

print(pn)


def solution(numbers):
    answer = 0

#미완