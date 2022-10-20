def solution(grade):
    count = 0
    min = grade[0]
    for i in range(1,len(grade)):
        s1,s2 = grade[i-1],grade[i]
        if s1 > s2:
            count += s1 - s2
            if s2 > min:
                count += (s2 - min) * 2
    return count




print(solution([3,8,6,1,7,4]))