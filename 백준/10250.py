# input = input().split()
# h = int(input[0])
# w = int(input[1])
# p = int(input[2])
#
# if p % h == 0:
#     pw = p
#     ph = h
# else:
#     pw = int(p / h + 1)
#     ph = p % h
#
# print(str(ph) + '0' + str(pw))
#
# try1

# input = input().split()
# h = int(input[0])
# w = int(input[1])
# p = int(input[2])
#
# if p % h == 0:
#     pw = p
#     ph = h
# else:
#     pw = int(p / h + 1)
#     ph = p % h
#
# r = ph*100+pw
#
# print(r)
#
# try2
# import sys
# a = int(input())
# for i in range(a):
#     l = (sys.stdin.readline().strip()).split(' ')
#     h = int(l[0])
#     w = int(l[1])
#     p = int(l[2])
#
#     if p % h == 0:
#         pw = w
#         ph = p/w
#     else:
#         pw = p%w
#         ph = int(p/w)+1
#
#     r = ph*100+pw
#
#     print(int(r))
#
# try 3

# import sys
# a = int(input())
# for i in range(a):
#     l = (sys.stdin.readline().strip()).split(' ')
#     h = int(l[0])
#     w = int(l[1])
#     p = int(l[2])
#
#     if p % h == 0:
#         pw = p/w
#         ph = w
#     else:
#         pw = int(p/w)+1
#         ph = p%w
#
#     r = ph*100+pw
#
#     print(int(r))
#
# try4

# import sys
#
# a = int(input())
# for i in range(a):
#     l = (sys.stdin.readline().strip()).split(' ')
#     h = int(l[0])
#     w = int(l[1])
#     p = int(l[2])
#
#     if p % h == 0:
#         pw = p / h
#         ph = h
#     else:
#         pw = int(p / w)
#         ph = p % w
#
#     r = ph * 100 + pw
#
#     print(int(r))
#
# try5


import sys

a = int(input())
for i in range(a):
    l = (sys.stdin.readline().strip()).split(' ')
    h = int(l[0])
    w = int(l[1])
    p = int(l[2])

    if p % h == 0:
        pw = p / h
        ph = h
    else:
        pw = int(p / h) + 1
        ph = p % h

    r = ph * 100 + pw

    print(int(r))

#머리가 복잡해졌을땐 그냥 잠깐 쉬다오자.........
