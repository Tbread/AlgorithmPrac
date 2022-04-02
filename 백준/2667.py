import sys


def find(arr, sx, sy, num):
    coords = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if arr[sx][sy] == 0:
        return arr, num
    arr[sx][sy] = 0
    num += 1
    for coord in coords:
        if 0 <= sx + coord[0] < len(arr) and len(arr) > sy + coord[1] >= 0:
            arr, num = find(arr, sx + coord[0], sy + coord[1], num)
    return arr, num


n = int(sys.stdin.readline())
map_arr = []
result = []
for _ in range(n):
    temp_list = list(sys.stdin.readline().strip())
    for i in range(len(temp_list)):
        temp_list[i] = int(temp_list[i])
    map_arr.append(temp_list)
for i in range(n):
    for j in range(n):
        map_arr,num = find(map_arr,i,j,0)
        if num != 0:
            result.append(num)
print(len(result))
result.sort()
for ea in result:
    print(ea)
