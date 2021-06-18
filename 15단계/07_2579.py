import sys
input = sys.stdin.readline

N = int(input())
score = [0 for _ in range(N+3)]
floor_score = [0 for _ in range(N+3)]
for k in range(1,N+1):
    floor_score[k] = int(input())


score [1] = floor_score[1]
score [2] = floor_score[1] + floor_score[2]
score [3] = max(floor_score[1] + floor_score[3] ,floor_score[2] + floor_score[3])


for i in range(4, N+1):
    score[i] = max( score[i-3] + floor_score[i-1] + floor_score[i] ,  score[i-2] + floor_score[i] )
print(score[N])