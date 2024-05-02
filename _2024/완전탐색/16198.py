# 16198 에너지 모으기

import sys
import copy
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
marbles = list(map(int,input().split()))
ans = 0

def solve(sum):
    if len(marbles) == 2:
        global ans
        ans = max(ans,sum)
        return
      
    for i in range(1,len(marbles)-1):
        next = marbles[i-1] * marbles[i+1]
        tmp = marbles.pop(i)
        solve(next+sum)
        marbles.insert(i,tmp)


solve(0)
print(ans)