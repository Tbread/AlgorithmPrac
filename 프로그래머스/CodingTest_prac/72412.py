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
    info_dict = {'java':[],'cpp':[],'python':[],'backend':[],'frontend':[],'junior':[],'senior':[],'chicken':[],'pizza':[]}
    for i in range(len(info)):
        if 'java' in info[i]:
            info_dict['java'].append(i)
        elif 'cpp' in info[i]:
            info_dict['cpp'].append(i)
        elif 'python' in info[i]:
            info_dict['java'].append(i)
        if 'backend' in info[i]:
            info_dict

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
