
def convert_times(lines):
    times = []
    for i in range(len(lines)):
        splitT = [lines[i].split()[1][:2], lines[i].split()[1][3:5], lines[i].split()[1][6:8], lines[i].split()[1][9:]]
        endT = int(splitT[0]) * 3600000 + int(splitT[1]) * 60000 + int(splitT[2]) * 1000 + int(splitT[3])
        workT = int(float(lines[i].split()[2][:-1]) * 1000)
        startT = endT - workT + 1
        times.append([startT, endT])
    return times


def solution(lines):
    times = convert_times(lines)
    mults = []
    for i in range(len(times)):
        mult = 1
        endT = times[i][1]
        for j in range(len(times)):
            if i == j:
                continue
            checkST,checkET = times[j][0],times[j][1]
            if checkST < endT + 1000 and endT <= checkET:
                mult += 1
        mults.append(mult)
    answer = max(mults)
    return answer






solution(["2016-09-15 20:59:57.421 0.351s",
          "2016-09-15 20:59:58.233 1.181s",
          "2016-09-15 20:59:58.299 0.8s",
          "2016-09-15 20:59:58.688 1.041s",
          "2016-09-15 20:59:59.591 1.412s",
          "2016-09-15 21:00:00.464 1.466s",
          "2016-09-15 21:00:00.741 1.581s",
          "2016-09-15 21:00:00.748 2.31s",
          "2016-09-15 21:00:00.966 0.381s",
          "2016-09-15 21:00:02.066 2.62s"])
