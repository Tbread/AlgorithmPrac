def solution(number, k):
    numbers = list(str(number))
    answer_list = []
    for num in numbers:
        if k > 0:
            if not answer_list:
                answer_list.append(num)
            else:
                while True:
                    if not answer_list:
                        answer_list.append(num)
                        break
                    if answer_list[-1] < num:
                        answer_list.pop()
                        k -= 1
                        if k == 0:
                            answer_list.append(num)
                            break
                    else:
                        answer_list.append(num)
                        break
        else:
            answer_list.append(num)
    if k > 0:
        for k in range (k):
            answer_list.pop()
    answer = ''.join(answer_list)
    return answer

