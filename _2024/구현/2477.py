# 2477 참외밭 실2

import sys
input = sys.stdin.readline

K = int(input())

the_map = [[] for _ in range(5)]

for _ in range(6):
    num, length = map(int,input().split())

    if num == 1 and len(the_map[2]) == 1 and length > the_map[2][0]:
        the_map[2].append(the_map[2][0])
        the_map[2][0] = 0

    if num == 2 and len(the_map[1]) == 1 and length > the_map[1][0]:
        the_map[1].append(the_map[1][0])
        the_map[1][0] = 0

    if num == 3 and len(the_map[4]) == 1 and length > the_map[4][0]:
        the_map[4].append(the_map[4][0])
        the_map[4][0] = 0

    if num == 4 and len(the_map[3]) == 1 and length > the_map[3][0]:
        the_map[3].append(the_map[3][0])
        the_map[3][0] = 0

    if len(the_map[num]) == 2:
        the_map[num][0] = length
    else:
        the_map[num].append(length)

width = 0
length = 0
area = 0

sm_width = 0
sm_length = 0
sm_area = 0

if len(the_map[1]) == 1:
    width = the_map[1][0]

    if len(the_map[4]) == 1:
        sm_width = the_map[2][1]
    else:
        sm_width = the_map[2][0]

else:
    width = the_map[2][0]

    if len(the_map[4]) == 1:
        sm_width = the_map[1][0]
    else:
        sm_width = the_map[1][1]

if len(the_map[3]) == 1:
    length = the_map[3][0]

    if len(the_map[2]) == 1:
        sm_length = the_map[4][0]
    else:
        sm_length = the_map[4][1]

else:
    length = the_map[4][0]

    if len(the_map[2]) == 1:
        sm_length = the_map[3][1]
    else:
        sm_length = the_map[3][0]

area = width * length
sm_area = sm_width * sm_length

result = (area - sm_area) * K

print(result)