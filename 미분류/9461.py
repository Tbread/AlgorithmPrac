# repeat = int(input())
#
# arr = [0,1,1,1,2,2,3]
# for _ in range(repeat):
#     a = int(input())
#     if a <= 6:
#         print(arr[a])
#     else:
#         for i in range(7,a+2):
#             arr.append(arr[i-5]+arr[i-1])
#         print(arr[a])
#
#try1 arr 초기화를 안해서 배열이 계속 중첩되고있었음...

repeat = int(input())

for _ in range(repeat):
    arr = [0, 1, 1, 1, 2, 2, 3]
    a = int(input())
    if a <= 6:
        print(arr[a])
    else:
        for i in range(7,a+2):
            arr.append(arr[i-5]+arr[i-1])
        print(arr[a])
