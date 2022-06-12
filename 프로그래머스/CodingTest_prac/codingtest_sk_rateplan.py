import copy
def solution(n, plans, clients):
    services = {}
    answers = []
    for i in range(len(plans)):
        plans[i] = list(map(int,plans[i].split(' ')))
        if i == 0:
            services[i] = []
        else:
            services[i] = copy.deepcopy(services[i-1])
        for j in range(1,len(plans[i])):
            services[i].append(plans[i][j])

    # 부가서비스 정렬 완

    for i in range(len(clients)):
        clients[i] = list(map(int,clients[i].split(' ')))
        min_plan = -1
        for m in range(len(plans)):
            if plans[m][0] >= clients[i][0]:
                min_plan = m
                break
        if min_plan == -1:
            answers.append(0)
            continue
        need_services = clients[i][1:]
        for m in range(len(services)):
            flag = 0
            for n in range(1,len(clients[i])):
                if not clients[i][n] in services[m]:
                    flag = 1
                    continue
            if flag == 0 and m >= min_plan:
                answers.append(m+1)
                break
        if flag == 1 or m < min_plan:
            answers.append(0)
    return answers




solution(4,["38 2 3","394 1 4"],["10 2 3","300 1 2 3 4","500 1"])