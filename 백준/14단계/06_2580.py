import sys
from collections import Counter

arr = []
arrh = []

for _ in range(9):
    arre = list(map(int, input().split()))
    arr.append(arre)
# for i in range(9):
#     arre = []
#     for j in range(9):
#         arre.append(arr[j][i])
#     arrh.append(arre)
breakchk = 0
while True:
    breakchk = 0
    for i in range(9):
        sumi = sum(arr[i])
        # if sumi <= 44 and sumi >= 36: #이렇게하면안되고 0개수를 세야할거같음
        #     this_idx = arr[i].index(0)
        #     arr[i][this_idx] = 45 - sumi
        if arr[i].count(0) == 1:
            this_idx = arr[i].index(0)
            arr[i][this_idx] = 45 - sumi

    arrh = []
    for i in range(9):
        arre = []
        for j in range(9):
            arre.append(arr[j][i])
        arrh.append(arre)
    # 세로열
    for i in range(9):
        sumi = sum(arrh[i])
        if arrh[i].count(0) == 1:
            this_idx = arrh[i].index(0)
            arrh[i][this_idx] = 45 - sumi
    arr = []

    for i in range(9):
        arre = []
        for j in range(9):
            arre.append(arrh[j][i])
        arr.append(arre)

    arrn = []
    arre = []
    c = 0
    d = 3
    for k in range(3):
        a = 0
        b = 3
        for m in range(3):
            for i in range(a, b):
                for j in range(c, d):
                    arre.append(arr[i][j])
            arrn.append(arre)
            arre = []
            a += 3
            b += 3
        c += 3
        d += 3
    # 블럭화

    for i in range(9):
        sumi = sum(arrn[i])
        if arrn[i].count(0) == 1:
            this_idx = arrn[i].index(0)
            arrn[i][this_idx] = 45 - sumi



    arr = []
    arre = []
    c = 0
    b = 3
    a = 0
    for k in range(3):
        for m in range(3):
            for i in range(a, 9,3):
                for j in range(c, c+3):
                    arre.append(arrn[i][j])
            arr.append(arre)
            arre = []
            c += 3
        c = 0
        a += 1


    # 블럭화해제


    # 종료조건
    for i in range(9):
        breakchk += sum(arr[i])
    if breakchk == 405:
        break

for i in range(9):
    print(*arr[i])


#해당방식으로만 채워질수없는판이있나봄...브루트포스를 사용한뒤 백트래킹을 해야할것같음
