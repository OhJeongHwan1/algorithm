import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int,input().split()))
cost = list(map(int,input().split()))

price = road[0] * cost[0]
min_cost = cost[0]

for i in range(1, N-1):
  if min_cost > cost[i]: 
    min_cost = cost[i] 
  
  price += min_cost * road[i]

print(price)