import itertools


def solution(needs, r):
    comb_dict = {}
    partCount = len(needs[0])
    if partCount == r:
        return len(needs)
    existPart = []
    parts = []
    for i in range(partCount):
        existPart.append(i)
    partCombinations = list(itertools.combinations(existPart, r))
    for need in needs:
        part = []
        for i in range(len(need)):
            if need[i] == 1:
                part.append(i)
        parts.append(part)
    for combination in partCombinations:
        comb_dict[combination] = 0
    for combination in partCombinations:
        for part in parts:
            flag = 0
            for i in range(len(part)):
                if not part[i] in combination:
                    flag = 1
                    break
            if flag == 0:
                comb_dict[combination] += 1
    return max(comb_dict.values())



solution([[1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]], 2)

# def solution(needs, r):
#     answer = 0
#     parts = []
#     count_dict = {}
#     counts = []
#     robots = []
#     for need in needs:
#         part = []
#         for i in range(len(need)):
#             if need[i] == 1:
#                 part.append(i)
#                 if i in count_dict:
#                     count_dict[i] += 1
#                 else:
#                     count_dict[i] = 1
#         parts.append(part)
#     for key,value in count_dict.items():
#         counts.append([key,value])
#     counts.sort(key=lambda x:-x[1])
#     for i in range(r):
#         robots.append(counts[i][0])
#     for part in parts:
#         flag = 0
#         for i in range(len(part)):
#             if not part[i] in robots:
#                 flag = 1
#                 break
#         if flag == 0:
#             answer += 1
#     return answer
