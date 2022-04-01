import sys

CountB = 0
CountW = 0


def findzero(array):
    global CountB
    global CountW
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            sum += array[i][j]
    if sum != len(array) ** 2:
        if len(array) == 1:
            CountW += 1
            return
        elif sum == 0:
            CountW += 1
            return
        else:
            entirearr = []
            for i in range(int(len(array) / 2)):
                arr = []
                for j in range(int(len(array) / 2)):
                    arr.append(array[i][j])
                entirearr.append(arr)
            findzero(entirearr)  # 2사분면

            entirearr = []
            for i in range(int(len(array) / 2)):  # i는 그대로유지
                arr = []
                for j in range(int(len(array) / 2), int(len(array))):
                    arr.append(array[i][j])
                entirearr.append(arr)
            findzero(entirearr)  # 1사분면

            entirearr = []
            for i in range(int(len(array) / 2), int(len(array))):
                arr = []
                for j in range(int(len(array) / 2)):  # j는 그대로 유지
                    arr.append(array[i][j])
                entirearr.append(arr)
            findzero(entirearr)  # 3사분면

            entirearr = []
            for i in range(int(len(array) / 2), int(len(array))):
                arr = []
                for j in range(int(len(array) / 2), int(len(array))):
                    arr.append(array[i][j])
                entirearr.append(arr)
            findzero(entirearr)  # 4사분면
    else:
        CountB += 1
        return


length = int(input())
entirearr = []
for rp in range(length):
    arr = list(map(int, sys.stdin.readline().split()))
    entirearr.append(arr)
findzero(entirearr)
print(CountW)
print(CountB)

#코드짜는내내 너무 재밌었던 문제