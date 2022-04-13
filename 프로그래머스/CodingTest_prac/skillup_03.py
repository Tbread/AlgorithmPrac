def solution(n, computers):
    connections = {}
    networks = []
    for i in range(n):
        connections[i] = set()
        for j in range(n):
            if computers[i][j] == 1:
                connections[i].add(j)
    for key, value in connections.items():
        for i in range(len(value)):
            connections[value[i]].update(value)
    # for key,value in connections.items():
    #     connections[key] = set(connections[key])
    for key, value in connections.items():
        networks.append(tuple(value))
    return len(set(networks))


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
