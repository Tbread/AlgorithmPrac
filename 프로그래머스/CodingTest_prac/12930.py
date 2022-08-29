def solution(s):
    s = list(s)
    turn = 0
    for i in range(len(s)):
        turn += 1
        if s[i] == ' ':
            turn = 0
            continue
        if turn % 2 == 1:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    return ''.join(s)