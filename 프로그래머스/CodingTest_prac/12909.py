def solution(s):
    arr = []
    for sp in s:
        if sp == '(':
            arr.append(sp)
        else:
            if not arr:
                return False
            else:
                arr.pop()
    return arr == []