import re


def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        word = word.lower()
        if re.search('^[a-z]',word):
            word = word.upper()[0] + word[1:]
        answer += ' ' + word
    return answer.lstrip()
print(solution('0a123Sd a as33d a2sd'))
