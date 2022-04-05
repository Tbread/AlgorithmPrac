def solution(s):
    if recursion(s):
        return 1
    return 0


def recursion(s):
    temp_length = len(s)
    if temp_length == 0:
        return True
    if temp_length == 1:
        return False
    for i in range(temp_length - 1):
        if s[i] == s[i+1]:
            s = s.replace(s[i]*2,'')
            break
    if len(s) == temp_length:
        return False
    if recursion(s):
        return True
    else:
        return False


print(solution('baabaa'))