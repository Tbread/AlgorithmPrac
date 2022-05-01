import itertools


def solution(orders, course):
    combs = []
    # menus = set()
    possible = {}
    for i in course:
        possible[i] = {}
    # for i in range(len(orders)):
    #     menus = menus.union(orders[i])
    # for ea in course:
    #     combs += list(itertools.combinations(menus, ea))
    # 주문들간에 들어가지않은 요리까지 계산할필요가없으니 아래코드로 변경
    for order in orders:
        for ea in course:
            combs += list(itertools.combinations(order,ea))
    for order in orders:
        for comb in combs:
            flag = 0
            for ele in comb:
                if not ele in order:
                    flag = 1
                    break
            if flag == 0:
                comb = sorted(comb)
                temp = ''
                for i in range(len(comb)):
                    temp += comb[i]
                if not temp in possible[len(temp)]:
                    possible[len(temp)][temp] = 1
                else:
                    possible[len(temp)][temp] += 1
    answer = []
    for i in course:
        for key,value in possible[i].items():
            if value == max(possible[i].values()) and value != 1:
                answer.append(key)
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
