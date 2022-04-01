arr = []
sum = [0]
def hanoi(count, startpoint, endpoint, assist):
    if count == 1:
        arr.append(str(startpoint)+' '+str(endpoint))
        sum[0] += 1
        return
    hanoi(count - 1, startpoint, assist, endpoint)
    arr.append(str(startpoint)+' '+str(endpoint))
    sum[0] += 1
    hanoi(count - 1, assist, endpoint, startpoint)

#어떤 알고리즘인지는 이해했는데 내가이해한게맞는지 헷갈리는상태 ㅜ

inp = int(input())
hanoi(inp,1,3,2)
print(sum[0])
for i in range(len(arr)):
    print(arr[i])
