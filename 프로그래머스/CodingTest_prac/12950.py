def solution(arr1, arr2):
    answer = arr1.copy()
    x,y = len(arr1[0]),len(arr1)
    for i in range(y):
        for j in range(x):
            answer[i][j] = arr1[i][j]+arr2[i][j]
    return answer
solution([[1,2],[2,3]],[[3,4],[5,6]])