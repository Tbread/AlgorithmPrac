def solution(nums):
    tot = len(nums)
    nums = list(set(nums))
    if len(nums) < tot // 2:
        return len(nums)
    else:
        return tot // 2
