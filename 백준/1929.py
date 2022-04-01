# import math
# import sys
# sqrt = math.sqrt
#
# def chk(get):
#     for i in range(2,int(sqrt(get))+1):
#         if get%i == 0:
#             return False
#     return True
#
# l = sys.stdin.readline().strip().split(' ')
# M = int(l[0])
# N = int(l[1])+1
#
# for i in range(M,N):
#     if chk(i) == True:
#         print(i)
#
# try1

import math
import sys
sqrt = math.sqrt

def chk(get):
    if get == 1:
        return False
    for i in range(2,int(sqrt(get))+1):
        if get%i == 0:
            return False
    return True

l = sys.stdin.readline().strip().split(' ')
M = int(l[0])
N = int(l[1])+1

for i in range(M,N):
    if chk(i) == True:
        print(i)