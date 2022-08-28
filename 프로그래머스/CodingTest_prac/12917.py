def solution(s):
    arr = list(s)
    arr.sort(key=lambda x:x,reverse=True)
    return ''.join(arr)