def solution(N, number):
    makes = []
    for i in range(1, 9):
        nums = set()
        nums.add(int(str(N) * i))
        for j in range(0, i - 1):
            for x in makes[j]:
                for y in makes[- j - 1]:
                    nums.add(x + y)
                    nums.add(x - y)
                    nums.add(x * y)
                    if y != 0:
                        nums.add(x // y)
        if number in nums:
            return i
        makes.append(nums)
    return -1

print(solution(5,12))
