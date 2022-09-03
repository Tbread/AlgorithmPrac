def solution(relation):
    arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr0 = [],[],[],[],[],[],[],[]
    for i in range(len(relation)):
        for j in range(len(relation[i])):
            try:
                arr0.append(relation[i][0])
                arr1.append(relation[i][1])
                arr2.append(relation[i][2])
                arr3.append(relation[i][3])
                arr4.append(relation[i][4])
                arr5.append(relation[i][5])
                arr6.append(relation[i][6])
                arr7.append(relation[i][7])
            except:
                pass
    print(arr0,arr1,arr2,arr3,arr4,arr5,arr6,arr7)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
