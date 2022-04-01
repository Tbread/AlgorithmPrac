repeat = int(input())
stack = []
sum = 0
for rp in range(repeat):
    callnum = int(input())
    if callnum == 0:
        stack.pop()
    else:
        stack.append(callnum)
for rp in range(len(stack)):
    sum += stack[rp]
print(sum)