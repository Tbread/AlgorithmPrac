def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    if a == 1:
        day = b - 1
    else:
        for i in range(a-1):
            day += days[i]
        day += b-1
    day %= 7
    if day == 0:
        return "FRI"
    elif day == 1:
        return "SAT"
    elif day == 2:
        return "SUN"
    elif day == 3:
        return "MON"
    elif day == 4:
        return "TUE"
    elif day == 5:
        return "WED"
    else:
        return "THU"

print(solution(5,24))