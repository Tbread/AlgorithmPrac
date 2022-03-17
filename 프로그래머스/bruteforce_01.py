def solution(answers):
    answer = []
    arr1 = []
    arr2 = []
    arr3 = []
    scores = [0,0,0]
    flag = 1
    for i in range(len(answers)):
        if flag > 5:
            flag = 1
        arr1.append(flag)
        flag += 1
    flag = 1
    for i in range(len(answers)):
        if flag > 8:
            flag = 1
        if flag % 2 == 1:
            arr2.append(2)
        elif flag == 2:
            arr2.append(1)
        elif flag == 4:
            arr2.append(3)
        elif flag == 6:
            arr2.append(4)
        elif flag == 8:
            arr2.append(5)
        flag += 1
    flag = 1
    for i in range(len(answers)):
        if flag > 10:
            flag = 1
        if flag == 1 or flag == 2:
            arr3.append(3)
        if flag == 3 or flag == 4:
            arr3.append(1)
        if flag == 5 or flag == 6:
            arr3.append(2)
        if flag == 7 or flag == 8:
            arr3.append(4)
        if flag == 9 or flag == 10:
            arr3.append(5)
        flag += 1
    for i in range(len(answers)):
        if arr1[i] == answers[i]:
            scores[0] += 1
        if arr2[i] == answers[i]:
            scores[1] += 1
        if arr3[i] == answers[i]:
            scores[2] += 1
    mx = max(scores)
    rp = 1
    for score in scores:
        if score == mx:
            answer.append(rp)
        rp += 1
    return answer