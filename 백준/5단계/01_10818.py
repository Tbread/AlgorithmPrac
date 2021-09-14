a = int(input())
b = input().split(' ')
num1 = int(b[0])
num2 = int(b[0])
for i in range(a):
    if num1 < int(b[i]):
        num1 = int(b[i])
for v in range(a):
    if num2 > int(b[v]):
        num2 = int(b[v])

print(num2,num1)

