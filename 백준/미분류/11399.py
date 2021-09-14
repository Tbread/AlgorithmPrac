peoples = int(input())
t = list(map(int,input().split()))
t.sort()

for i in range(1,peoples):
    t[i] += t[i-1]

print(sum(t))