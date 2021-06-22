
result_arr = []
tmp_arr1 = [1,0]
tmp_arr2 = [0,1]
result_arr.append(tmp_arr1)
result_arr.append(tmp_arr2)
for i in range(2,41):
    tmp_arr = []
    tmp_arr.append(result_arr[i-2][0]+result_arr[i-1][0])
    tmp_arr.append(result_arr[i-2][1]+result_arr[i-1][1])
    result_arr.append(tmp_arr)

repeat = int(input())

for _ in range(repeat):
    a = int(input())
    print(*result_arr[a])

# 항상까먹는다...재귀함수를 직접 만들필요없이 그냥 나는 빠르게 결과를 뽑아낼수있는 계산식을 찾도록록 하자