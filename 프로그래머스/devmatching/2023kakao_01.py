def solution(today, terms, privacies):
    answer = []
    t = {}
    today = list(map(int, today.split('.')))
    for i in range(len(terms)):
        t[terms[i].split()[0]] = int(terms[i].split()[1])
    for i in range(len(privacies)):
        days = list(map(int, privacies[i].split()[0].split('.')))
        condition = privacies[i].split()[1]
        days[1] = days[1] + t[condition]
        if days[1] > 12:
            while days[1] > 12:
                days[0] += 1
                days[1] -= 12
        if days[2] == 1:
            days[1] -= 1
            days[2] = 28
        else:
            days[2] -= 1
        if days[0] < today[0]:
            answer.append(i + 1)
            continue
        if days[0] == today[0]:
            if days[1] < today[1]:
                answer.append(i + 1)
                continue
            if days[1] == today[1]:
                if days[2] < today[2]:
                    answer.append(i + 1)
    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
