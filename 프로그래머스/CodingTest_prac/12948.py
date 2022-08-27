def solution(phone_number):
    slen = len(phone_number)
    splen = slen -4
    return ('*' * splen + phone_number[slen-4:])