# 11052 카드 구매하기
import sys

N = int(input())
card_pack = list(map(int,input().split()))

max_cost = [0 for _ in range(N+1)]

for i in range(N):
    if card_pack[i] > max_cost[i+1]:
        max_cost[i+1] = card_pack[i]
    for j in range(i+2,N+1):
        if max_cost[j-(i+1)] + card_pack[i] > max_cost[j]:
            max_cost[j] = max_cost[j-(i+1)] + card_pack[i]

print(max_cost[N])