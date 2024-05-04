# 27172 수 나누기 게임 골 5
# 에라토스테네스의 체

import sys
input = sys.stdin.readline

N = int(input())

players = list(map(int,input().split()))
the_max = max(players)
S = set(players)
results = [0 for _ in range(the_max+1)]

for player in players:
    if player == the_max: continue

    for j in range(2*player,the_max+1,player):
        if j in S:
            results[player] +=1
            results[j] -=1 

for player in players:
    print(results[player], end = ' ')