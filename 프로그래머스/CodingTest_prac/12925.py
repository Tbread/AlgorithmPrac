def solution(s):
    s = list(s)
    if s[0] == '+':
        return int(''.join(s[1:]))
    elif s[0] == '-':
        return -int(''.join(s[1:]))
    else:
        return int(''.join(s))