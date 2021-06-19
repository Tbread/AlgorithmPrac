N=int(input())
M=int(input())
V=1
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

for i in range(1,N+1):
    arr2.append(i)

dfs(V)
print(len(arr)-1)