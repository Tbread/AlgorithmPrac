arr = []
for i in range(9):
    arr.append(int(input()))
num = arr[0]
for i in range(9):
    if num < arr[i]:
        num = int(arr[i])

print(num)
print(arr.index(num)+1)