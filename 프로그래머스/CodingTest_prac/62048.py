def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)


def solution(w,h):
    gd = gcd(w,h)
    return w*h - (w+h - gd)
