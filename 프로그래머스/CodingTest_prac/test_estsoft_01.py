import heapq


def solution(scores):
    answer = 0
    headCount = len(scores[0])
    for score in scores:
        fCount = 0
        aCount = 0
        totScore = []
        totScoreNeg = []
        for i in range(len(score)):
            if score[i] == 'A':
                aCount += 1
                totScore.append(5)
                totScoreNeg.append(-5)
            elif score[i] == 'B':
                totScore.append(4)
                totScoreNeg.append(-4)
            elif score[i] == 'C':
                totScore.append(3)
                totScoreNeg.append(-3)
            elif score[i] == 'D':
                totScore.append(2)
                totScoreNeg.append(-2)
            elif score[i] == 'E':
                totScore.append(1)
                totScoreNeg.append(-1)
            else:
                totScore.append(0)
                totScoreNeg.append(0)
                fCount += 1
                if fCount == 2:
                    break
        if fCount == 2:
            continue
        elif aCount >= 2:
            answer += 1
            continue
        heapq.heapify(totScore)
        heapq.heapify(totScoreNeg)
        total = sum(totScore) - heapq.heappop(totScore) + heapq.heappop(totScoreNeg)
        if (total // (headCount - 2)) >= 3:
            answer += 1
    return answer


solution(["BCD", "ABB", "FEE"])
