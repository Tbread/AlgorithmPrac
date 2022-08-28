def solution(a, b):
    if b < a:
        a,b = b,a
    if (b - a + 1) % 2 == 0:
        return (a + b) * ((b - a + 1) // 2)
    else:
        return (a + b) * ((b - a + 1) // 2) + ((a + b) // 2)
