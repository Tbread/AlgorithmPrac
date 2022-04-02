def solution(n, edges, k, a, b):
    node_dict = make_dict(edges)
    line = len(edges)
    for key, value in node_dict.items():
        node_dict[key] = set(value)
    temp_routes = dfs_paths(node_dict, a, b)
    need_routes = []
    for temp_route in temp_routes:
        if len(temp_route) <= k+1:
            need_routes.append(temp_route)
    for need_route in need_routes:
        for i in range(len(need_route)-1):
            temp1 = [need_route[i+1],need_route[i]]
            temp2 = [need_route[i],need_route[i+1]]
            if temp1 in edges:
                edges.pop(edges.index(temp1))
            if temp2 in edges:
                edges.pop(edges.index(temp2))
    print(line-len(edges))
    return line-len(edges)


def dfs_paths(node_dict, start, end):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == end:
            result.append(path)
        else:
            for m in node_dict[n] - set(path):
                stack.append((m, path + [m]))
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
    return node_dict


solution(8, [[0, 1], [1, 2], [2, 3], [4, 0], [5, 1], [6, 1], [7, 2], [7, 3], [4, 5], [5, 6], [6, 7]], 4, 0, 3)
