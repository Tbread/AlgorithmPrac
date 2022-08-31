# def solution(info, query):
#     data = []
#     for i in info:
#         temp = i.split()
#         if temp[0] == 'cpp':
#             temp[0] = 0
#         elif temp[0] == 'java':
#             temp[0] = 1
#         else:
#             temp[0] = 2
#         if temp[1] == 'backend':
#             temp[1] = 0
#         else:
#             temp[1] = 1
#         if temp[2] == 'junior':
#             temp[2] = 0
#         else:
#             temp[2] = 1
#         if temp[3] == 'chicken':
#             temp[3] = 0
#         else:
#             temp[3] = 1
#         temp[4] = int(temp[4])
#         data.append(temp)
#     for i in range(len(query)):
#         temp = query[i].split(' and ')
#         if temp[0] == 'cpp':
#             temp[0] = 0
#         elif temp[0] == 'java':
#             temp[0] = 1
#         elif temp[0] == 'python':
#             temp[0] = 2
#         else:
#             temp[0] = -1
#         if temp[1] == 'backend':
#             temp[1] = 0
#         elif temp[1] == 'frontend':
#             temp[1] = 1
#         else:
#             temp[1] = -1
#         if temp[2] == 'junior':
#             temp[2] = 0
#         elif temp[2] == 'senior':
#             temp[2] = 1
#         else:
#             temp[2] = -1
#         temp[3] = temp[3].split(' ')
#         temp.append(int(temp[3][1]))
#         if temp[3][0] == 'chicken':
#             temp[3] = 0
#         elif temp[3][0] == 'pizza':
#             temp[3] = 1
#         else:
#             temp[3] = -1
#         query[i] = temp
#     answer = []
#     for i in range(len(query)):
#         cnt = 0
#         for j in range(len(data)):
#             flag = 0
#             for m in range(5):
#                 if m != 4:
#                     if query[i][m] == data[j][m] or query[i][m] == -1:
#                         pass
#                     else:
#                         flag = 1
#                         break
#                 else:
#                     if query[i][m] <= data[j][m]:
#                         pass
#                     else:
#                         flag = 1
#                         break
#             if flag == 0:
#                 cnt += 1
#             flag = 0
#         answer.append(cnt)
#         cnt = 0
#     return answer


def solution(info, query):
    answer = []
    info_dict = {'java': [], 'cpp': [], 'python': [], 'backend': [], 'frontend': [], 'junior': [], 'senior': [],
                 'chicken': [], 'pizza': [], 'score': []}
    for i in range(len(info)):
        if 'java' in info[i]:
            info_dict['java'].append(i)
        elif 'cpp' in info[i]:
            info_dict['cpp'].append(i)
        elif 'python' in info[i]:
            info_dict['python'].append(i)
        if 'backend' in info[i]:
            info_dict['backend'].append(i)
        else:
            info_dict['frontend'].append(i)
        if 'junior' in info[i]:
            info_dict['junior'].append(i)
        else:
            info_dict['senior'].append(i)
        if 'chicken' in info[i]:
            info_dict['chicken'].append(i)
        else:
            info_dict['pizza'].append(i)
        info_dict['score'].append([int(info[i].split(' ')[4]), i])
    start = 0
    for q in query:
        q = q.replace(' and ', ' ').split(' ')
        # elif min >= q[4]:
        #     start = 0
        # else:
        #     start = len(info_dict['score'])//2
        #     if info_dict['score'][start][0] < q[4]:
        #         while info_dict['score'][start][0] < q[4]:
        #             start += 1
        #     else:
        #         while info_dict['score'][start][0] >= q[4]:
        #             start -= 1
        #         start += 1
        con1 = []
        con2 = []
        con3 = []
        con4 = []
        if q[0] == 'java':
            con1 = info_dict['java']
        elif q[0] == 'python':
            con1 = info_dict['python']
        elif q[0] == 'cpp':
            con1 = info_dict['cpp']
        else:
            con1 = info_dict['java'] + info_dict['python'] + info_dict['cpp']
        if q[1] == 'backend':
            con2 = info_dict['backend']
        elif q[1] == 'frontend':
            con2 = info_dict['frontend']
        else:
            con2 = info_dict['backend'] + info_dict['frontend']
        if q[2] == 'junior':
            con3 = info_dict['junior']
        elif q[2] == 'senior':
            con3 = info_dict['senior']
        else:
            con3 = info_dict['junior'] + info_dict['senior']
        if q[3] == 'pizza':
            con4 = info_dict['pizza']
        elif q[3] == 'chicken':
            con4 = info_dict['chicken']
        else:
            con4 = info_dict['pizza'] + info_dict['chicken']
        con1, con2, con3, con4 = set(con1), set(con2), set(con3), set(con4)
        fit = list(con1 & con2 & con3 & con4)
        if not fit:
            answer.append(0)
            continue
        temp = 0
        for i in fit:
            if info_dict['score'][i][0] >= int(q[4]):
                temp += 1
        answer.append(temp)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
