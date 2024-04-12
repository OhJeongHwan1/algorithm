# 2138 전구와 스위치
# 아주 신선한 그리디

import sys
input = sys.stdin.readline

N = int(input())
start = list(input().strip())
goal = list(input().strip())



def change(now,cnt):
    count = 0
    for i in range(1,N):
        if now[i-1] != goal[i-1]:
            count += 1
            if i == N-1:
                now[i-1] = '0' if now[i-1] == '1' else '1'
                now[i] = '0' if now[i] == '1' else '1'
                break
            now[i-1] = '0' if now[i-1] == '1' else '1'
            now[i] = '0' if now[i] == '1' else '1'
            now[i+1] = '0' if now[i+1] == '1' else '1'

    if now == goal:
        return count + cnt
    else:
        return -1

if start == goal:
    print(0)
else:
    change_start = start.copy()
    result = change(start,0)
    if result == -1:
        change_start[0] = '0' if change_start[0] == '1' else '1'
        change_start[1] = '0' if change_start[1] == '1' else '1'
        result = change(change_start,1)
        print(result)
    else:
        print(result)