def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result


def solution(grid, k):
    node = {}
    for i in range(1, len(grid) * len(grid[0]) + 1):
        node[i] = []
        y = len(grid)
        x = len(grid[0])
    for i in range(y):
        for j in range(x):
            if grid[i][j] == "#":
                continue
            if j + 1 < x:
                if grid[i][j + 1] == "F" or grid[i][j + 1] == ".":
                    node[(i * x) + (j + 1)].append((i * x) + (j + 1) + 1)
            if j - 1 >= 0:
                if grid[i][j - 1] == "F" or grid[i][j - 1] == ".":
                    node[(i * x) + (j + 1)].append((i * x) + (j + 1) - 1)
            if i + 1 < y:
                if grid[i + 1][j] == "F" or grid[i + 1][j] == ".":
                    node[(i * x) + (j + 1)].append(((i + 1) * x) + j + 1)
            if i - 1 >= 0:
                if grid[i - 1][j] == "F" or grid[i - 1][j] == ".":
                    node[(i * x) + (j + 1)].append(((i - 1) * x) + j + 1)
    # 경로 노드화
    for key, value in node.items():
        node[key] = set(value)
    routes = bfs_paths(node, 1, x * y)
    # 모든경로 가져오기

    temp_str = ""
    for i in range(len(grid)):
        temp_str += grid[i]
    listing = list(temp_str)
    route_views = []
    for i in range(len(routes)):
        temp_str = ''
        for j in range(len(routes[i])):
            temp_str += listing[routes[i][j] - 1]
        route_views.append(temp_str)
    # 루트 가시화
    rest_arr = []
    print(route_views)
    for i in range(len(route_views)):
        warn_str = 'F' * k
        if warn_str in route_views[i]:
            continue
            # 불가능한 루트
        temp_arr = route_views[i].split('.')
        temp_arr = temp_arr[1:]
        rest = 0
        flag = 0
        for m in range(len(temp_arr)):
            flag += len(temp_arr[m])+1
            if flag > k:
                rest += 1
                flag = len(temp_arr[m])
                print(flag)
        rest_arr.append(rest)
    return min(rest_arr)


solution(
    ["..FF", "###F", "###."], 5)
