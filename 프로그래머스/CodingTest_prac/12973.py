def solution(s):
    arr = []
    for ele in s:
        if not arr:
            arr.append(ele)
        elif arr[-1] == ele:
            arr.pop()
        else:
            arr.append(ele)
    if arr:
        return 0
    return 1

print(solution('baabaa'))
