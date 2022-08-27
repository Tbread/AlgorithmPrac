import heapq


def solution(N, stages):
    stage_arr = []
    clear_dict = {}
    block_dict = {}
    for i in range(1, N + 1):
        stage_arr.append([i,-1])
        clear_dict[i] = 0
        block_dict[i] = 0
    for i in range(len(stages)):
        stages[i] = -stages[i]
    heapq.heapify(stages)
    totalnum = 0
    allclear = 0
    while stages:
        bstage = -heapq.heappop(stages)
        if bstage > N:
            allclear += 1
        elif clear_dict[bstage] == 0:
            clear_dict[bstage] = totalnum + 1
            block_dict[bstage] = 1
        else:
            block_dict[bstage] += 1
            clear_dict[bstage] += 1
        totalnum += 1
    for i in range(1,N+1):
        if block_dict[i] == 0:
            if i != N:
                clear_dict[i] = clear_dict[i+1]
            else:
                clear_dict[i] = allclear
        if clear_dict[i] != 0:
            stage_arr[i-1][1] = block_dict[i] / clear_dict[i]
        else:
            stage_arr[i-1][1] = 0
    stage_arr.sort(key=lambda x:(-x[1],x[0]))
    answer =[]
    for i in stage_arr:
        answer.append(i[0])
    return answer



# def solution(N, stages):
#     for i in range(len(stages)):
#         stages[i] = -stages[i]
#     points = []
#     heapq.heapify(stages)
#     cs_dict = {}
#     sp_dict = {}
#     tempnum = 0
#     fp_arr = []
#     while stages:
#         cs = heapq.heappop(stages)
#         if -cs > N:
#             pass
#         elif -cs in cs_dict:
#             cs_dict[-cs] += 1
#             sp_dict[-cs] += 1
#         else:
#             cs_dict[-cs] = 1
#             sp_dict[-cs] = tempnum + 1
#             points.append(-cs)
#         tempnum += 1
#     for i in points:
#         cs = cs_dict[i]
#         sp = sp_dict[i]
#         fp = cs/sp
#         fp_arr.append([i,fp])
#     answer = []
#     for i in range(1,N+1):
#         if i in points:
#             continue
#         else:
#             fp_arr.append([i,0])
#     fp_arr.sort(key=lambda x:(-x[1],x[0]))
#     for i in range(len(fp_arr)):
#         answer.append(fp_arr[i][0])
#     print(answer)


solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3])
