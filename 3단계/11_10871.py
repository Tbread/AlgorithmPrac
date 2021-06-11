import sys

userinput = input().split(' ')
a = int(userinput[0])
b = int(userinput[1])

l = (sys.stdin.readline().strip()).split(' ')


for i in range(a):
    if int(l[i]) < b:
        print(l[i])