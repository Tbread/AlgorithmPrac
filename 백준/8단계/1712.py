# ip = input().split()
# sad = int(ip[0])
# a = int(ip[1])
# b = int(ip[2])
# bene = b - a
# realbene = 0 - sad
# i = 0
# if a > b:
#     print(-1)
# else:
#     while True:
#         i += 1
#         realbene += bene
#         if realbene > 0:
#             break
# print(i)
#try1


ip = input().split()
sad = int(ip[0])
a = int(ip[1])
b = int(ip[2])
bene = b - a
i = 0
if a >= b:
    print(-1)
else:
    i = (sad/bene)+1
    print(int(i))