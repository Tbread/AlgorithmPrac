def solution(dartResult):
    dartResult = dartResult.replace('S','S.').replace('D','D.').replace('T','T.').replace('*','*.').replace('#','#.').split('.')
    for i in range(len(dartResult)):
        if 'S' in dartResult[i] or 'D' in dartResult[i] or 'T' in dartResult[i]:
            dartResult[i] = eval(dartResult[i].replace('S','**1').replace('D','**2').replace('T','**3'))

    place = 0
    score = []
    temp = 0
    for i in range(len(dartResult)):
        if type(dartResult[i]) is int:
            if temp != 0:
                score.append(temp)
                place += 1
            temp = str(dartResult[i])
        elif type(dartResult[i]) is str:
            if dartResult[i] == '*':
                temp += '*2'
                if place != 0:
                    score[place-1] += '*2'
            elif dartResult[i] == '#':
                temp += '*-1'
            else:
                score.append(temp)
    for i in range(len(score)):
        score[i] = eval(score[i])

    return sum(score)




solution('1S*2T*3S')