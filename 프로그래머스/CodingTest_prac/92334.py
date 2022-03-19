def solution(id_list, report, k):
    report = list(set(report))
    reported_num = {}
    email_num = {}
    ban_id_list = []
    answer = []
    for i in range(len(report)):
        report[i] = report[i].split(' ')
    for id in id_list:
        reported_num[id] = 0
        email_num[id] = 0
    for reported in report:
        reported_num[reported[1]] += 1
    for key, value in reported_num.items():
        if value >= k:
            ban_id_list.append(key)
    for ban_id in ban_id_list:
        for reported in report:
            if reported[1] == ban_id:
                email_num[reported[0]] += 1
    for key, value in email_num.items():
        answer.append(value)
    return answer
