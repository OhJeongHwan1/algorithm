# 부분수열의 합2 골1
# 중요한 풀이!! 
# 배열을 반으로 나누어 각각에 대한 부분수열의 합을 생성한 후 
# 투 포인터로 두 값을 더하면서 진행한다.

import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int,input().split())
ans = 0
arr = list(map(int,input().split()))

arr1 = arr[:N//2]
arr2 = arr[N//2:]

left = []
right = []

for i in range(len(arr1)+1):
    for com in combinations(arr1,i):
        left.append(sum(com))
left.sort()

for i in range(len(arr2)+1):
    for com in combinations(arr2,i):
        right.append(sum(com))
right.sort(reverse=True)

lp = 0
rp = 0

while lp < len(left) and rp < len(right):
    sum = left[lp] + right[rp]

    if sum < S:
        lp += 1
    elif sum > S:
        rp += 1
    else:
        x = 1 
        for i in range(lp+1,len(left)):
            if left[lp] == left[i]:
                x += 1
            else: break
        
        y = 1
        for i in range(rp+1,len(right)):
            if right[rp] == right[i]:
                y += 1
            else: break
        ans += x*y
        lp += x
        rp += y
        
if S == 0:
    print(ans-1)
else:
    print(ans)