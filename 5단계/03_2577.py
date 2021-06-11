arr = []
for i in range(3):
    arr.append(int(input()))

tot = arr[0]*arr[1]*arr[2]
arr2 = list(str(tot))
chkarr = [0] * 10
for char in arr2:
    i = ord(char)-48
    chkarr[i] += 1
for i in range(len(chkarr)):
    print(chkarr[i])


