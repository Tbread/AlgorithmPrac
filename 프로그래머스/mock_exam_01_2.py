def solution(want, number, discount):
    least = 100000
    for i in range(len(want)):
        if discount.count(want[i]) < number[i]:
            return 0
    for need in want:
        for i in range(len(discount)):
            if discount[i] == need:
                if i < least:
                    least = i
                break
    for i in range(least,len(discount)-9):
        flag = 0
        print(discount[i:i+10])
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) < number[j]:
                flag = 1
                break
        if flag == 1:
            continue
        return i+1
    return 0


print(solution(["banana"], [1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
          "apple", "tai"]))
