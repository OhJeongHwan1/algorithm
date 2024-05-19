# 7453 합이 0인 네 정수 골2
# 정렬 이분탐색

import sys

input = sys.stdin.readline

N = int(input())
ans = 0
the_list = [list(map(int,input().split())) for _ in range(N)]
before_list = []
for i in range(N):
    for j in range(N):
        before_list.append(the_list[i][0]+the_list[j][1])

after_list = []

for i in range(N):
    for j in range(N):
        after_list.append(the_list[i][2]+the_list[j][3])
before_list.sort()
after_list.sort()

left = 0
right = len(after_list) - 1

while 0 <= right and left < len(before_list):
    sum = before_list[left] + after_list[right]

    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        x = 1
        for i in range(left+1,len(before_list)):
            if before_list[i] == before_list[left]:
                x += 1
            else:
                break
        y = 1
        for i in range(right-1,-1,-1):
            if after_list[i] == after_list[right]:
                y += 1
            else:
                break

        ans += x*y
        left += x
        right -= y

print(ans)