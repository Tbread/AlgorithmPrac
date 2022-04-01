import sys
n, m = map(int, sys.stdin.readline().strip().split(' '))
inp = [[''] * m for _ in range(n)]
arr = []
answer1,answer2 = 0,0
for i in range(n):
    inp[i] = list(sys.stdin.readline().strip())

for i in range(n - 7):
    for j in range(m - 7):
        for x in range(i,i + 8):
            for y in range(j,j + 8):
                if (x + y) % 2 == 0:
                    if inp[x][y] != 'W':
                        answer1 += 1
                    else:
                        answer2 += 1
                else:
                    if inp[x][y] != 'B':
                        answer1 += 1
                    else:
                        answer2 += 1
        arr.append(answer1)
        arr.append(answer2)
        answer1,answer2 = 0,0

print(min(arr))

