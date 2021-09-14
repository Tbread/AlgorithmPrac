# import sys
# N,M,V = map(int, sys.stdin.readline().split())
# L = []
# for i in range(M):
#     L.append(list(map(int, sys.stdin.readline().split())))
#
# L.sort(key=lambda x:(x[0],x[1]))
#
#
# now = V
# traveled = 0
# O = []
# while traveled != N:
#     tempL = []
#     for i in range(M):
#         if L[i][0] == now:
#             tempL.append(L[i])
#         print(tempL)
#     tralveled += 1
#     O.append

N,M,V=map(int,input().split())
chk=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    chk[a][b]=chk[b][a]=1
VL=[0]*(N+1)
arr=[]
arr2=[]
def dfs(V):
    VL[V]=1 
    arr.append(V)
    for i in range(1,N+1):
        if(VL[i]==0 and chk[V][i]==1):
            dfs(i)

def bfs(V):
    todo=[V]
    VL[V]=0
    while todo:
        V=todo.pop(0)
        arr2.append(V)
        for i in range(1, N+1):
            if(VL[i]==1 and chk[V][i]==1):
                todo.append(i)
                VL[i]=0

dfs(V)
bfs(V)
print(*arr)
print(*arr2)