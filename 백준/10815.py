import sys

n = int(sys.stdin.readline().strip())

arr1 = set(sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())

arr2 = set(sys.stdin.readline().strip().split())

answer = []
for ele in arr2:
    if ele in arr1:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))