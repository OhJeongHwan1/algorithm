# 11053 가장 긴 증가하는 부분 수열

import sys
N = int(input())

num_array = list(map(int, sys.stdin.readline().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i,N):
        if num_array[i] < num_array[j]:
            if dp[j] < dp[i]+1:
                dp[j] = dp[i]+1

print(max(dp))