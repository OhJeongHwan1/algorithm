import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
card = list(map(int,(input().split())))
cards =[]
for num in card:
    heapq.heappush(cards, num)

while m > 0:
    newCard = int(heapq.heappop(cards)) + int(heapq.heappop(cards))
    heapq.heappush(cards, newCard)
    heapq.heappush(cards, newCard)
    m = m-1

print(sum(cards))