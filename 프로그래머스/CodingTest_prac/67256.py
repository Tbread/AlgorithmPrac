def solution(numbers, hand):
    answer = ''
    position = [[3, 0], [3, 2]]
    buttons = []
    num_dict = {}
    for i in range(4):
        for j in range(3):
            buttons.append([i, j])
    for i in range(len(numbers)):
        numbers[i] = numbers[i] - 1
        if numbers[i] == -1:
            numbers[i] = 10
    for i in range(12):
        num_dict[i] = buttons[i]
    for number in numbers:
        L = position[0]
        R = position[1]
        if number % 3 == 0:
            answer += 'L'
            position[0] = num_dict[number]
        elif number % 3 == 2:
            answer += 'R'
            position[1] = num_dict[number]
        else:
            if abs(L[0] - num_dict[number][0]) + abs(L[1] - num_dict[number][1]) < abs(R[0] - num_dict[number][0]) + abs(R[1] - num_dict[number][1]):
                answer += 'L'
                position[0] = num_dict[number]
            elif abs(L[0] - num_dict[number][0]) + abs(L[1] - num_dict[number][1]) > abs(R[0] - num_dict[number][0]) + abs(R[1] - num_dict[number][1]):
                answer += 'R'
                position[1] = num_dict[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    position[0] = num_dict[number]
                else:
                    answer += 'R'
                    position[1] = num_dict[number]
    return answer
