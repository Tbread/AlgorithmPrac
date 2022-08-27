def solution(n, arr1, arr2):
    map = []
    for i in range(len(arr1)):
        arr1[i], arr2[i] = bin(arr1[i])[2:], bin(arr2[i])[2:]
        while len(arr1[i]) < n:
            arr1[i] = '0' + arr1[i]
        while len(arr2[i]) < n:
            arr2[i] = '0' + arr2[i]
        arr1[i], arr2[i] = int('1' + arr1[i]), int('1' + arr2[i])
        temp = str(arr1[i] + arr2[i])[1:].replace('1', '#').replace('2', '#').replace('0', ' ')
        map.append(temp)
    return map


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
