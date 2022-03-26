def solution(numbers):
    numbers = list(map(str,numbers))
    arr = []
    answer = ''
    for number in numbers:
        arr.append([int(number),number[0]])
    arr.sort(key=lambda x:(x[1],x[0]),reverse=True)
    for string in arr:
        answer += str(string[0])
    return answer
print(solution([3, 30, 34, 5, 9]))

#미완