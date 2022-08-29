def solution(x):
    y = list(str(x))
    sum = 0
    for num in y:
        sum += int(num)
    if x%sum == 0:
        return True
    return False