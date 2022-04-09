import heapq

def solution(array, commands):
    answers = []
    for command in commands:
        temp_arr = array[command[0] - 1:command[1]]
        heapq.heapify(temp_arr)
        for i in range(command[2]):
            k = heapq.heappop(temp_arr)
        answers.append(k)
        temp_arr = []
    return answers

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))