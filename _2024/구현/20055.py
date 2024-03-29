# 20055 컨베이어 벨트 위의 로봇 골 5
# 신경써서 볼 부분은 체크하는 부분을 매번 다하지 말고 필요할 때만 해서
# 성능향상 시켜줘야 할 필요 있음.

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
the_list = list(map(int,input().split()))
belt = deque()
the_robot = [ False for _ in range(N)]
is_robots = deque()
result = 0

for index in the_list:
    belt.append(index)

for robot in the_robot:
    is_robots.append(robot)

the_count = 0

while True:
    belt.appendleft(belt.pop())
    is_robots.pop()
    is_robots.appendleft(False)

    for i in range(N-1,0,-1):
        if i == N - 1:
            if is_robots[i] == True:
                is_robots[i] = False
        else:
            if is_robots[i] == True and is_robots[i+1] == False and belt[i+1] >= 1:
                is_robots[i] = False
                is_robots[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    the_count += 1

    if belt[0] >= 1 and is_robots[0] == False:
        is_robots[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            the_count += 1

    result += 1

    if the_count >= K:
        break

print(result)
