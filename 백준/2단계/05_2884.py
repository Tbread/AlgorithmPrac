userinput = input().split(' ')
a = int(userinput[0])
b = int(userinput[1])
if b < 45:
    a -= 1
    if a < 0:
        a = 23
    b = (60-45+b)
else:
    b -= 45

print(a,b)