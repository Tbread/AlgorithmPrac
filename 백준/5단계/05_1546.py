import sys
a = int(input())
l = (sys.stdin.readline().strip()).split(' ')
num = int(l[0])
sum = 0
for i in range(a):
    if int(num) < int(l[i]):
        num = l[i]
for i in range(a):
    l[i] = (int(l[i])/int(num))*100
    sum += l[i]
print(sum/int(a))