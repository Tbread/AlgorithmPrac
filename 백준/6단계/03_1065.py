a = int(input())
m = 0
for i in range(1, a + 1):
    if i < 100:
        m += 1
    else:
        aa = list(str(i))
        if int(aa[2])-int(aa[1]) == int(aa[1])-int(aa[0]):
            m +=1

print(m)