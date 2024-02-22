# 2294 동전 2

import sys

input = sys.stdin.readline
INF = float("inf")
N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]
dp = [ INF for _ in range(K+1) ]

if min(coins) > K:
    print(-1)
    exit()

for coin in coins:
    if coin > K:
        continue
    dp[coin] = 1

    for index in range(coin,K+1):
        # print(index)
        if index == coin:
            continue
        if dp[index] > dp[index-coin] + 1:
            dp[index] = dp[index-coin] + 1

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
        
