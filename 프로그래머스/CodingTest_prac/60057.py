def solution(s):
    if len(s) == 1:
        return 1
    answer = 0
    sliced = ''
    sliced_dict = {}
    while True:
        sliced,sliced_dict = find_slice(s,sliced_dict)
        if sliced:
            sliced_dict,s = sliced_over(s,sliced,sliced_dict)
        else:
            break
    for key,value in sliced_dict.items():
        answer += len(key)+len(str(value))
    answer += len(s)
    return answer

def find_slice(s,sliced_dict):
    sliced = ''
    for i in range(len(s),int(len(s)/2)+1):
        temp_str = s[:i+1]
        if s[i+1:].startswith(temp_str):
            sliced = temp_str
    if sliced:
        sliced_dict[sliced] = 1
        return sliced,sliced_dict
    return sliced,sliced_dict

def sliced_over(s,sliced,sliced_dict):
    while True:
        if s[len(sliced):].startswith(sliced):
            sliced_dict[sliced] += 1
            s = s[len(sliced):]
        else:
            s = s[len(sliced):]
            break
    return sliced_dict,s


print(solution('abcabcabcabcdededededede'))