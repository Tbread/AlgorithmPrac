def solution(price, money, count):
    if count % 2 == 0:
        n = (count + 1) * (count // 2)
    else:
        n = (count + 1) * (count // 2) + (count // 2) + 1
    less = n*price - money
    if less <= 0:
        return 0
    else:
        return less