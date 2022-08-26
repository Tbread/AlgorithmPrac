def solution(survey, choices):
    score_dict = {}
    score_dict['R'] = 0
    score_dict['T'] = 0
    score_dict['C'] = 0
    score_dict['F'] = 0
    score_dict['J'] = 0
    score_dict['M'] = 0
    score_dict['A'] = 0
    score_dict['N'] = 0
    for i in range(len(survey)):
        if choices[i] == 1:
            score_dict[survey[i][0]] += 3
        elif choices[i] == 2:
            score_dict[survey[i][0]] += 2
        elif choices[i] == 3:
            score_dict[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            score_dict[survey[i][1]] += 1
        elif choices[i] == 6:
            score_dict[survey[i][1]] += 2
        elif choices[i] == 7:
            score_dict[survey[i][1]] += 3

    answer = ''
    if score_dict['R'] >= score_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if score_dict['C'] >= score_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if score_dict['J'] >= score_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score_dict['A'] >= score_dict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
