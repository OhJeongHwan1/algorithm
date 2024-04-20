# 2467 용액 

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
liquieds = list(map(int,input().split()))

start = 0
end = N-1
min = 10000000000
ans_list = []
while start < end:
    sum = liquieds[start] + liquieds[end]
    if abs(sum) < min:
        min = abs(sum)
        ans_list = [liquieds[start],liquieds[end]]
    else:
        #print(start,end,liquieds[start],liquieds[end],sum,min)
        if sum > 0:
            end -= 1
        elif sum < 0:
            start += 1
        else:
            min = sum
            ans_list = [liquieds[start],liquieds[end]]
            break

print(*ans_list)
        