import sys

nm = list(map(int, sys.stdin.readline().strip().split()))

nums = list(map(int, sys.stdin.readline().strip().split()))
sums = []
init = 0
for i in range(len(nums)):
    sums.append(init+nums[i])
    init += nums[i]

for _ in range(nm[1]):
    ij = list(map(int, sys.stdin.readline().strip().split()))
    end = sums[ij[1]-1]
    start = sums[ij[0]-1]
    print(end-start+nums[ij[0]-1])
