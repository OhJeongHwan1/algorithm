# 국회의원 선거 실 5
import sys
import heapq
input = sys.stdin.readline
N = int(input())
hubo = [int(input()) for _ in range(N)]

dasom = hubo[0]
hubo = hubo[1:]
ans = 0

queue = []
for i in range(N-1):
    heapq.heappush(queue,-hubo[i])

if len(hubo) == 0:
    print(0)
    exit()

while True:
    other = -heapq.heappop(queue)
    if other >= dasom:
        dasom += 1
        other -= 1
        ans += 1
        heapq.heappush(queue,-other)
    else:
        break

print(ans)