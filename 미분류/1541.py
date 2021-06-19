#그냥 첫 - 가 나오는순간 뒤에있는 숫자를 싹다 빼주면됨

str = input()

str = str.replace('+',' ')


l = str.split('-')

for i in range(len(l)):
    l[i] = list(map(int,l[i].split()))
    l[i] = sum(l[i])

if len(l) == 1:
    print(l[0])
else:
    sum = 0
    for i in range(1,len(l)):
        sum += l[i]
    print(l[0] - sum)