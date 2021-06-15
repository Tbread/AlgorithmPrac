from collections import deque
while True:
    string = input()
    if string == '.':
        break
    ls = list(string)
    deq = deque()
    mod_deq = deque()
    for i in ls:
        deq.append(i)
    for i in range(len(deq)):
        if deq[0] == '(' or deq[0] == '[' or deq[0] == ')' or deq[0] == ']':
            mod_deq.append(deq[0])
        deq.popleft()
    str = ''.join(mod_deq)
    while True:
        post_str_last = str
        while True:
            post_str = str.replace('()','')
            if post_str == str:
                break
            str = post_str

        while True:
            post_str = str.replace('[]','')
            if post_str == str:
                break
            str = post_str
        if post_str_last == str:
            str = post_str_last
            break

    if str == '':
        print('yes')
    else:
        print('no')

