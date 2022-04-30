def solution(places):
    answer = []
    for i in range(5):
        temp_place = []
        checked = []
        for j in range(5):
            temp = places[i][j]
            temp_place.append(list(temp))
        for y in range(5):
            for x in range(5):
                if [x,y] in checked:
                    continue
                else:



solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
