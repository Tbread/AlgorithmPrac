# import copy
#
#
# def solution(arr, processes):
#     taskmgr = []
#     for i in range(len(processes)):
#         processes[i] = processes[i].split(' ')
#     tasks = copy.deepcopy(processes)
#     for task in processes:
#         if task[0] == 'read':
#             taskmgr, processes = read_task(taskmgr, tasks, processes, task)
#             idx = tasks.index(task)
#             for i in range(int(task[2])):
#                 taskmgr.append(idx + 1)
#             idx = processes.index(task)
#             processes[idx][0] = 'done'
#         elif task[0] == 'write':
#             idx = tasks.index(task)
#             for i in range(int(task[2])):
#                 taskmgr.append(idx + 1)
#             idx = processes.index(task)
#             processes[idx][0] = 'done'
#     # print(taskmgr)
#     worked_arr = working(arr, list(set(taskmgr)), tasks)
#     worked_arr.append(len(taskmgr))
#     print(taskmgr)
#     return worked_arr
#
# def read_task(taskmgr, tasks, processes, task):
#     # print('read_task')
#     arr = []
#     for t in processes:
#         # print(len(taskmgr),int(t[1]),int(task[1]),t[0])
#         if len(taskmgr) < int(t[1]) < int(task[1]) and t[0] == 'write':
#             idx = tasks.index(t)
#             for i in range(t[2]):
#                 taskmgr.append(idx + 1)
#             idx = processes.index(t)
#             processes[idx][0] = 'done'
#             break
#         if int(t[1]) > int(task[1]):
#             break
#     if find_write(taskmgr, processes, task):
#         taskmgr, processes = read_task(taskmgr, tasks, processes, task)
#     return taskmgr, processes
#
#
# def find_write(taskmgr, processes, task):
#     # print('find_write')
#     for t in processes:
#         if len(taskmgr) < int(t[1]) < int(task[1]) and t[0] == 'write':
#             return True
#         if int(t[1]) > int(task[1]):
#             return False
#         return False
#
#
# def working(arr, taskmgr, tasks):
#     worked_arr = []
#     for task in taskmgr:
#         if tasks[task - 1][0] == 'read':
#             temp_str = ''
#             for i in range(int(tasks[task-1][3]),int(tasks[task-1][4])+1):
#                 temp_str += arr[i]
#             worked_arr.append(temp_str)
#         else:
#             for i in range(int(tasks[task-1][3]),int(tasks[task-1][4])+1):
#                 arr[i] = tasks[task-1][5]
#     return worked_arr
#
#

import copy


# def solution(arr, processes):
#     taskmgr = []
#     wait = []
#     for i in range(len(processes)):
#         processes[i] = processes[i].split(' ')
#     tasks = copy.deepcopy(processes)
#     for task in processes:
#         if len(taskmgr) == 0:
#             for i in range(int(task[2])):
#                 idx = processes.index(task)
#                 temp_str = task[0][0]
#                 taskmgr.append(temp_str + str(idx))
#             continue
#         if len(taskmgr) > int(task[1]):
#             if task[0] == 'write':
#                 if len(wait) == 0:
#                     idx = processes.index(task)
#                     for i in range(int(task[2])):
#                         taskmgr.append('w'+str(idx))
#                 else:
#                     #대기열이있을때
#             elif task[0] == 'read':
#                 if len(wait) == 0:
#                     idx = processes.index(task)
#                     for i in range()
#     return taskmgr
# print(solution(["1", "2", "4", "3", "3", "4", "1", "5"],
#          ["read 1 3 1 2",
#           "read 2 6 4 7",
#           "write 4 3 3 5 2",
#           "read 5 2 2 5",
#           "write 6 1 3 3 9",
#           "read 9 1 0 7"]))

def solution(arr, processes):
    taskmgr = []
    wait = []
    wip = []
    mx_time = 0
    for i in range(len(processes)):
        processes[i] = processes[i].split(' ')
    tasks = copy.deepcopy(processes)
    for task in processes:
        mx_time += int(task[2])