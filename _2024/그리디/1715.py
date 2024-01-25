# 1715 카드 정렬하기
# 우선순위 큐 사용해서 가장 작은 값끼리 더하기

import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []
answer = 0

for _ in range(N):
    heapq.heappush(hq,int(input()))

while len(hq) > 1:
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)

    sum = num1 + num2
    answer += sum

    heapq.heappush(hq,sum)

print(answer)
