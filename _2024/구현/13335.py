# 13335 트럭

import sys
from collections import deque
input = sys.stdin.readline

n,w,l = map(int, input().split())
trucks = list(map(int,input().split()))
queue = deque()

for _ in range(w):
    queue.append(0)

time = 0
weights = 0

while True:
    time += 1
    old = queue.popleft()
    weights -= old

    if len(trucks) != 0:
        new = trucks[0]
        weights += new

        if weights <= l:
            new_truck = trucks.pop(0)
            queue.append(new_truck)
        else:
            queue.append(0)
            weights -= new

    else:
        queue.append(0)

    if len(trucks) == 0 and max(queue) == 0:
        break

print(time)


    