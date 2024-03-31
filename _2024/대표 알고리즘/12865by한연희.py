# 12865 평범한 배낭 골5
# knapsack problem 예전에 배운 알고리즘으로는 시간 초과 발생함.

import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())

products = []

for _ in range(N):
    w, v = map(int,input().split())
    v_per_w = v/w
    products.append([w,v,v_per_w])

products.sort(key=lambda x:-x[2])

def get_bound(rest_k,number):
    k = rest_k
    bound = 0
    for i in range(number,N):
        num = k - products[i][0]
        if num > 0:
            k = k - products[i][0]
            bound += products[i][1]
        elif num == 0:
            k = k - products[i][0]
            bound += products[i][1]
            break
        else:
            bound += products[i][2] * (k) 
            break

    return bound 

#queue = deque()
#queue.append([0,products[0][1],K-products[0][0],products[0][1] + get_bound(K-products[0][0],1)])
#queue.append([0,0,K, get_bound(K,1)])

heap = []
heapq.heappush(heap, [-(products[0][1] + get_bound(K-products[0][0],1)),0,products[0][1],K-products[0][0]])
heapq.heappush(heap, [-(get_bound(K,1)),0,0,K])

result = products[0][1]

while heap:
    #before, now_weight, rest_k, max_bound = queue.popleft()
    #print(heap)
    max_bound, before, now_weight, rest_k = heapq.heappop(heap)
    #print(-max_bound, before, now_weight, rest_k)

    if -(max_bound) <= result:
        continue

    result = max(result,now_weight)

    next = before + 1

    if next >= N:
        continue

    if rest_k - products[next][0] < 0:
        if now_weight + get_bound(rest_k,next + 1) > result:
            #queue.append([next,now_weight,rest_k,now_weight + get_bound(rest_k,next + 1)])
            heapq.heappush(heap, [-(now_weight + get_bound(rest_k,next + 1)),next,now_weight,rest_k])
    else:
        if now_weight + products[next][1] + get_bound(rest_k-products[next][0],next+1) > result:    
            #queue.append([next,now_weight + products[next][1],rest_k-products[next][0],now_weight + products[next][1] + get_bound(rest_k-products[next][0],next+1)])
            heapq.heappush(heap, [-(now_weight + products[next][1] + get_bound(rest_k-products[next][0],next+1)),next,now_weight + products[next][1],rest_k-products[next][0]])
        if now_weight + get_bound(rest_k,next + 1) > result:
            #queue.append([next,now_weight,rest_k,now_weight + get_bound(rest_k,next + 1)])
            heapq.heappush(heap, [-(now_weight + get_bound(rest_k,next + 1)),next,now_weight,rest_k])

print(result)