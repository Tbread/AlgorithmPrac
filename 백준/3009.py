from collections import Counter

arr = []
for _ in range(3):
    a = list(map(int, input().split()))
    arr.append(a)
x = []
y = []
for i in range(3):
    x.append(arr[i][0])
    y.append(arr[i][1])

x = str(Counter(x).most_common()[1]).replace(', 1','').replace('(','').replace(')','')
y = str(Counter(y).most_common()[1]).replace(', 1','').replace('(','').replace(')','')
print(x,y)