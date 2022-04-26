def solution(s):
    answer = []
    tuples = s.lstrip('{').rstrip('}').replace('},{', ' ').split(' ')
    for i in range(len(tuples)):
        tuples[i] = tuples[i].split(',')
        for j in range(len(tuples[i])):
            tuples[i][j] = int(tuples[i][j])
    tuples.sort(key=len)
    for i in range(len(tuples)):
        for j in range(len(tuples[i])):
            if tuples[i][j] in answer:
                continue
            answer.append(tuples[i][j])
    return answer


solution('{{1,2,3},{2,1},{1,2,4,3},{2}}')
