# 0 -> 0
# 1 -> 1
# 2 -> f0+f1+1 = 0,1,1
# 3 -> (f0+f1+1)+f1 = 0,1,1,1
# 4 -> (f0+f1+1)+f1+(f0+f1+1) = 0,1,1,1,0,1,1
# z=0
# o=0
# def fb(n):
#     global z
#     global o
#     if n == 0:
#         z += 1
#     elif n== 1:
#         o +=1
#     elif n>=2:
#         fb(n-1)
#         fb(n-2)
#
# repeat = int(input())
# for _ in range(repeat):
#     z = 0
#     o = 0
#     fb(int(input()))
#     print(z,o)

#
#try 1 시간초과


# z=0
# o=0
# pre_arr = []
# pre_arr_sub = []
# def fb(n):
#     global z
#     global o
#     if n == 0:
#         z += 1
#     elif n== 1:
#         o +=1
#     elif n>=2:
#         fb(n-1)
#         fb(n-2)
#
# for i in range(0,41):
#     pre_arr_sub = []
#     z = 0
#     o = 0
#     fb(i)
#     pre_arr_sub.append(z)
#     pre_arr_sub.append(o)
#     pre_arr.append(pre_arr_sub)
#
#
# 미리 구해놓고 출력하는식으로 할랬는데 n이 30을 넘어가는순간 급격하게 느려짐
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