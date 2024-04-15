# 10775 공항 골2
# Union-find 새로운 알고리즘 두 요소가 같은 집합에 있는지
# 확인하는 알고리즘

import sys

def find(u):
    if p[u]<0:
        return u
    
    p[u]=find(p[u])
    return p[u]

def union(u,v): # u가 루트
    u,v = find(u),find(v)

    if u==v :
        return

    p[v]=u
    
G, P = int(input()) , int(input())
p=[-1 for i in range(G+1)]
ans=0
for i in range(P):
    g = int(input())
    target = find(g)
    if target==0:
        break
    union(target-1, target)
    ans+=1
    
print(ans)