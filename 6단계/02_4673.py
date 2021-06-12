arr1=[]
arr2=[]
for i in range(1,10001):
    aa = list(str(i))
    m = 0
    for v in aa:
        m += int(v)
    r = m + i
    arr1.append(r)
    arr2.append(i)

comp = list(set(arr2).difference(arr1))
comp.sort()
for i in comp:
    print(i)