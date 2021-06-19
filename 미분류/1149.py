#색을 처음부터 정하지말고 케이스를 a,b,c로 분류해서 숫자가많은순서대로 작은비용에 할당하면 될듯
#아니다 조건을보니 조금다른듯

N = int(input())
arr= []
for _ in range(N):
    cost = sys.stdin.readline().strip().split(' ')
    arr.append(cost)

