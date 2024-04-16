# 1717 집합의 표현 골5
# 분리 집합의 근본

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int,input().split())

the_union = [i for i in range(n+1)]

def find(a):
    if a != the_union[a]:
        the_union[a] = find(the_union[a])
    return the_union[a]

def union(a,b):
    the_union[find(b)] = find(a)

for _ in range(m):  
    the_type, a, b = map(int,input().split())

    if the_type == 0:
        union(a,b)
    if the_type == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
            
