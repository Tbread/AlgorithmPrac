# # a = int(input())
# #
# # if a >= 5:
# #     five = int(a / 5)
# #     chk = a % 5
# #     if chk == 0:
# #         print(five)
# #     else:
# #         chk2 = chk % 3
# #         if chk2 != 0:
# #             print('-1')
# #         else:
# #             three = int(chk / 3)
# #             print(five + three)
# # else:
# #     chk = a % 3
# #     if chk != 0:
# #         print('-1')
# #     else:
# #         print(a / 3)
# #
# # try1
#
# # a = int(input())
# #
# # if a >= 5:
# #     five = int(a / 5)
# #     chk = a % 5
# #     if chk == 0:
# #         print(five)
# #     else:
# #         chk2 = chk % 3
# #         if chk2 != 0:
# #             chk3 = a % 3
# #             if chk3 != 0:
# #                 print('-1',1)
# #             else:
# #                 print(int(a/3))
# #         else:
# #             three = int(chk / 3)
# #             print(five + three)
# # else:
# #     chk = a % 3
# #     if chk != 0:
# #         print('-1',2)
# #     else:
# #         print(a / 3)
# #
# # try2
#
# a = int(input())
# flag = 0
# if a >= 5:
#     five = int(a / 5)
#     chk = a % 5
#     if chk == 0:
#         print(five)
#     else:
#         chk2 = chk % 3
#         if chk2 != 0:
#             chk3 = a % 3
#             if chk3 != 0:
#                 for i in range(1, int(a / 3) + 1):
#                     chk4 = a - (i * 3)
#                     if chk4 % 5 == 0:
#                         three = i
#                 if three > 0:
#                     a = a - (three * 3)
#                     five = int(a / 5)
#                     print(five + three)
#                 else:
#                     print('-1')
#             else:
#                 print(int(a / 3))
#         else:
#             three = int(chk / 3)
#             print(five + three)
# else:
#     chk = a % 3
#     if chk != 0:
#         print('-1')
#     else:
#         print(a / 3)
#
# try3

# for a in range(3,5000):
#     # a = int(input())
#     if a >= 5:
#         five = int(a / 5)
#         chk = a % 5
#         if chk == 0:
#             print(five,'케이스1')
#         else:
#             chk2 = a % 3
#             if chk2 != 0:
#                 chk3 = a % 3
#                 if chk3 != 0:
#                     for i in range(1, int(a / 3) + 1):
#                         chk4 = a - (i * 3)
#                         if chk4 % 5 == 0:
#                             three = i
#                     if three > 0:
#                         a = a - (three * 3)
#                         five = int(a / 5)
#                         if five > 0:
#                             print(five + three,'케이스2')
#                     else:
#                         print('-1','케이스4')
#                 else:
#                     print(int(a / 3))
#             else:
#                 three = int(a / 3)
#                 print(three,'케이스5')
#     else:
#         chk = a % 3
#         if chk != 0:
#             print('-1','케이스6')
#         else:
#             print(int(a / 3),'케이스7')
#
#
# try4

i = int(input())
answer = 0
# for i in range(3,5001):
if i == 3:
    answer = 1
    print(answer)
elif i == 4:
    answer = -1
    print(answer)
elif i == 5:
    answer = 1
    print(answer)
else:
    if i % 5 == 0:
        answer = i / 5
        print(int(answer))
    elif i % 3 == 0:
        five = int(i / 5)
        chk = i - (five * 5)
        if chk % 3 == 0:
            three = int(chk / 3)
            answer = five + three
            print(int(answer))
        else:
            for v in range(int(i / 5), 0, -1):
                chk = i - (v * 5)
                if chk % 3 == 0:
                    answer = v + int(chk / 3)
                    print(int(answer))
                    break
            if answer == 0:
                answer = i / 3
                print(int(answer))
    elif i / 5 >= 1 and i % 5 != 0:
        chkfive = int(i / 5)
        chk = i - (chkfive * 5)
        if chk % 3 == 0:
            answer = int(i / 5) + int(chk / 3)
            print(int(answer))
        else:
            for v in range(1, int(i / 3) + 1):
                chk = i - (v * 3)
                if chk % 5 == 0:
                    answer = v + int(chk / 5)
                    print(int(answer))
                    break
                else:
                    answer = -1
            if answer == -1:
                print(answer)
