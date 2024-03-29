# 18111 마인 크래프트
# 높이 마다 걸리는 시간을 배열을 생성하여 저장한다.
# 이건 복습을 해야할 수준임...
# 풀 지 못한 문제임

import sys

input = sys.stdin.readline

N, M, B = map(int,input().split())

ground = []
for _ in range(N):
    ground.extend(map(int, input().split()))

time = [0 for i in range(257)] # time[k]에 땅높이가 k일때의 소요시간 저장
height = 0
for g in range(257):
    block = B # 인벤토리에 남은 블록 수
    for i in ground:
        if i <= g: # i == g이면 g-i=0
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    if block >= 0 and time[g] <= time[height]: # 오름차순으로 순회하므로, 답이 여러 개 있을 때 그중에서 땅의 높이가 가장 높은 것을 저장하게 됨
        height = g # 최소 소요 시간인 땅높이 저장

print(time[height], height)

