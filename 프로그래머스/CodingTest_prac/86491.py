def solution(sizes):
    templong = 0
    tempshort = 0
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            if templong < sizes[i][0]:
                templong = sizes[i][0]
            if tempshort < sizes[i][1]:
                tempshort = sizes[i][1]
        else:
            if templong < sizes[i][1]:
                templong = sizes[i][1]
            if tempshort < sizes[i][0]:
                tempshort = sizes[i][0]
    return tempshort * templong


