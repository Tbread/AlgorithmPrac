import re


def solution(s):
    if (len(s) == 4 or len(s) == 6) and re.sub('\d', '', s) == '':
        return True
    return False


print(solution('14d335'))
