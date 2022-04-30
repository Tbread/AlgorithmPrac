def solution(answers):
    correct = [0,0,0]
    answer = []
    answers_length = len(answers)
    arr1 = [1, 2, 3, 4, 5] * (answers_length // 5 + 1)
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5] * (answers_length // 8 + 1)
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (answers_length // 10 + 1)
    for i in range(answers_length):
        if answers[i] == arr1[i]:
            correct[0] += 1
        if answers[i] == arr2[i]:
            correct[1] += 1
        if answers[i] == arr3[i]:
            correct[2] += 1
    for i in range(3):
        if correct[i] == max(correct):
            answer.append(i+1)
    return answer

