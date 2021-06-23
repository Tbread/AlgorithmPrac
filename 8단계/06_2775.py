# h = int(input())
# w = int(input())
# p = 0
# apart = [[0 for we in range(w)] for he in range(h)]
#
# for i in range(w):
#     apart[0][i] = i + 1
#
#
#
# print(apart)
# for i in range(1,h):  # 층반복
#     for v in range(w):
#         if v == 0:
#             apart[i][v] = 1
#             print('1호라서 1을 집어넣었습니다')
#         else:
#             for vn in range(v-1):
#                 apart[i][v] = apart[i][v] + apart[i][vn]
#                 print(apart)
#
#
#     apart[i][0] = 1
#     print(apart)
#
def first_floor(num,num2): #num = 층 num2 =호
    if num == 1:
        return num2
    return first_floor(num-1,num2)

def nth_floor(num,num2):
    if num2 == 1:
        return first_floor(num)
    if num == 1:
        return 1
    return first_floor(num) + nth_floor(num-1,num2)

print(first_floor(2,3))