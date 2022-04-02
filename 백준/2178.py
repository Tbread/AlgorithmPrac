import sys
from collections import deque

import heapq

# from collections import OrderedDict


def dijkstra(graph, first, last):
    distance = {node: [float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []
    path_output = 0

    heapq.heappush(queue, [distance[first][0], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node][0]:
                # 다음 노드까지 총 거리와 어떤 노드를 통해서 왔는지 입력
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])
    # 마지막 노드부터 첫번째 노드까지 순서대로 출력
    path = last
    path_output += 1
    while distance[path][1] != first:
        path_output += 1
        path = distance[path][1]
    path_output += 1
    return path_output
    # return distance


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
            print(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result


def make_dict(edges):
    node_dict = {}
    for elements in edges:
        if not elements[0] in node_dict:
            node_dict[elements[0]] = []
            node_dict[elements[0]].append(elements[1])
        else:
            node_dict[elements[0]].append(elements[1])
        if not elements[1] in node_dict:
            node_dict[elements[1]] = []
            node_dict[elements[1]].append(elements[0])
        else:
            node_dict[elements[1]].append(elements[0])
    # node_dict = OrderedDict(sorted(node_dict.items(), key=lambda x: x[0]))
    return node_dict

def make_double_dict(edges):
    node_dict = {}
    for elements in edges:
        if not elements[0] in node_dict:
            node_dict[elements[0]] = {}
            node_dict[elements[0]][elements[1]]=1
        else:
            node_dict[elements[0]][elements[1]]=1
        if not elements[1] in node_dict:
            node_dict[elements[1]] = {}
            node_dict[elements[1]][elements[0]]=1
        else:
            node_dict[elements[1]][elements[0]]=1
    # node_dict = OrderedDict(sorted(node_dict.items(), key=lambda x: x[0]))
    return node_dict


def convert_edge(arr, sx, sy, check, x, y, edges):
    coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for coord in coords:
        if (0 <= sy + coord[0] < y) and (0 <= sx + coord[1] < x):
            if [[sy + coord[0]], [sx + coord[1]]] in check:
                continue
            check.append([[sy + coord[0]], [sx + coord[1]]])
            if arr[sy + coord[0]][sx + coord[1]] == 0:
                continue
            if [sy * x + sx, ((sy + coord[0]) * x) + sx + coord[1]] in edges or [((sy + coord[0]) * x) + sx + coord[1],
                                                                                 sy * x + sx] in edges:
                continue

            edges.append([sy * x + sx, ((sy + coord[0]) * x) + sx + coord[1]])
            arr, check, edges = convert_edge(arr, sx + coord[1], sy + coord[0], check, x, y, edges)
    return arr, check, edges


def dfs_paths(node_dict, start, end):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == end:
            result.append(len(path))
        else:
            for m in node_dict[n] - set(path):
                stack.append((m, path + [m]))
    return result


y, x = map(int, sys.stdin.readline().split())
arr = []
check = []
edges = []
for i in range(y):
    arr.append(list(sys.stdin.readline().strip()))
    for j in range(x):
        arr[i][j] = int(arr[i][j])
for i in range(y):
    for j in range(x):
        if [i, j] in check:
            continue
        check.append([i, j])
        if arr[i][j] == 0:
            continue
        arr, check, edges = convert_edge(arr, j, i, check, x, y, edges)
# for i in range(len(edges)):
#     if edges[i][0] > edges[i][1]:
#         edges[i] = [edges[i][1],edges[i][0]]
node_dict = make_double_dict(edges)
# for key, value in node_dict.items():
#     node_dict[key] = set(value)
result = dijkstra(node_dict, 0, (x*y)-1)
print(result)
