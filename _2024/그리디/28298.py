# 더 흔한 타일 색칠 문제 실3
import sys

tiles = [] # N * M 타일
count_list = [0] * 26 # 알파벳의 개수를 count해주는 리스트
Sum = 0 # 교체한 타일 개수

N, M, K = map(int, input().split())
for i in range(N):
    tiles.append(list(sys.stdin.readline().rstrip()))

step_num = N * M // K**2 # K * K 로 나눈 개수

for x in range(K):
    for y in range(K): # K * K 판에서 각각의 자리

        count_list = [0] * 26 # 개수 count 리스트 초기화

        for i in range(0, N - K+ 1, K):
            for j in range(0, M - K + 1, K): 
                t = tiles[i + x][j + y]
                count_list[ord(t) - 65] += 1 # 알파벳 count

        max_tile_num = max(count_list) 
        Sum += step_num - max_tile_num # 변경한 타일 개수 추가
        max_tile = chr(count_list.index(max_tile_num) + 65) #가장 개수가 많은 알파벳 return

        for i in range(0, N - K+ 1, K):
            for j in range(0, M - K + 1, K):
                tiles[i + x][j + y] = max_tile # 타일 변환

# 출력
print(Sum)
for line in tiles:
    print("".join(line))