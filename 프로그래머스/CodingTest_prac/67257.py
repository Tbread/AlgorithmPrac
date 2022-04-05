import re,copy


def counting_all(os, ns):
    arr = []
    signs = [os,ns]
    arr.append(multiply(minus(plus(copy.deepcopy(signs))))[1][0])
    arr.append(plus(multiply(minus(copy.deepcopy(signs))))[1][0])
    arr.append(plus(minus(multiply(copy.deepcopy(signs))))[1][0])
    arr.append(minus(plus(multiply(copy.deepcopy(signs))))[1][0])
    arr.append(minus(multiply(plus(copy.deepcopy(signs))))[1][0])
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    return max(arr)


def minus(signs):
    order_sign, num_sign = signs[0], signs[1]
    for i in range(len(order_sign)):
        if i == len(order_sign):
            if order_sign:
                minus([order_sign,num_sign])
            break
        if order_sign[i] == '-':
            temp1 = num_sign[i]
            temp2 = num_sign[i + 1]
            num_sign[i] = temp1 - temp2
            del num_sign[i + 1]
            del order_sign[i]
            if '-' not in order_sign:
                break
    return [order_sign, num_sign]


def multiply(signs):
    order_sign, num_sign = signs[0], signs[1]
    for i in range(len(order_sign)):
        if i == len(order_sign):
            if order_sign:
                multiply([order_sign, num_sign])
            break
        if order_sign[i] == '*':
            temp1 = num_sign[i]
            temp2 = num_sign[i + 1]
            num_sign[i] = temp1 * temp2
            del num_sign[i + 1]
            del order_sign[i]
            if '*' not in order_sign:
                break
    return [order_sign, num_sign]


def plus(signs):
    order_sign, num_sign = signs[0], signs[1]
    for i in range(len(order_sign)):
        if i == len(order_sign):
            if order_sign:
                plus([order_sign, num_sign])
            break
        if order_sign[i] == '+':
            temp1 = num_sign[i]
            temp2 = num_sign[i + 1]
            num_sign[i] = temp1 + temp2
            del num_sign[i + 1]
            del order_sign[i]
            if '+' not in order_sign:
                break
    return [order_sign, num_sign]


def solution(s):
    order_sign = list(re.sub('[0-9]', '', s))
    num_sign = s.replace('-', ' ').replace('+', ' ').replace('*', ' ').split(' ')
    for i in range(len(num_sign)):
        num_sign[i] = int(num_sign[i])
    answer = counting_all(order_sign,num_sign)
    return answer
