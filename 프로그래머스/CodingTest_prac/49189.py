def graphing(edges):
    node_graph = {}
    for edge in edges:
        if edge[0] in node_graph:
            node_graph[edge[0]].append(edge[1])
        else:
            node_graph[edge[0]] = [edge[1]]
        if edge[1] in node_graph:
            node_graph[edge[1]].append(edge[0])
        else:
            node_graph[edge[1]] = [edge[0]]
    return node_graph

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            return len(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))

def solution(n, edges):
    node_graph = graphing(edges)
    for key,value in node_graph.items():
        node_graph[key] = set(value)
    distance = []
    for i in range(2,n+1):
        distance.append(bfs_path(node_graph,1,i))
    return distance.count(max(distance))


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])