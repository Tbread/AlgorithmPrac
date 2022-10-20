def check(world, x, y, n):
    if world[y][x + 1] == 0:
        world[y][x + 1] = 3
        n += 1
        world,n = check(world,x+1,y,n)
    if world[y][x - 1] == 0:
        world[y][x - 1] = 3
        n += 1
        world,n = check(world,x-1,y,n)
    if world[y+1][x] == 0:
        world[y+1][x] = 3
        n += 1
        world,n = check(world,x,y+1,n)
    if world[y-1][x] == 0:
        world[y-1][x] = 3
        n += 1
        world,n = check(world,x,y-1,n)
    return world,n


def solution(rows, columns, lands):
    world = [[0] * columns for i in range(rows)]
    for i in range(len(lands)):
        world[lands[i][0] - 1][lands[i][1] - 1] = 1
    for y in range(len(world)):
        for x in range(len(world[0])):
            if x == 0 or x == len(world[0]) - 1:
                world[y][x] = 2
            if y == 0 or y == len(world) - 1:
                world[y][x] = 2
    for y in range(len(world)):
        for x in range(len(world[0])):
            if world[y][x] == 0:
                if world[y - 1][x] == 2 or world[y][x - 1] == 2 or world[y + 1][x] == 2 or world[y][x + 1] == 2:
                    world[y][x] == -1
                else:
                    world[y][x] == 3
                    world,n = check(world,0,0,1)
    print(n)
    for i in range(len(world)):
        print(world[i])


solution(9,7,[[2,2],[2,3],[2,5],[3,2],[3,4],[3,5],[3,6],[4,3],[4,6],[5,2],[5,5],[6,2],[6,3],[6,4],[6,6],[7,2],[7,6],[8,3],[8,4],[8,5]])