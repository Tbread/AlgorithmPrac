a = input()
i = 0
comp = a
final = '100'
b = a
arr=[0,0]
while (int(final) != int(comp)):
    if (int(a) < 10):
        a = str(0) + a
    i += 1
    num1 = list(a)[-2]
    num2 = list(a)[-1]
    sum = int(num1)+int(num2)
    num3 = list(str(sum))[-1]
    arr[0] = num2
    arr[1] = num3
    final = str(num2) + str(num3)
    a = final
print(i)