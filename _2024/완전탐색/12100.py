# 12100 2048 이지 버전
# 추후에 다시 도전
# 백트래킹 브루트 포스

import sys

input = sys.stdin.readline

N = int(input())

board = [ list(map(int,input().split())) for _ in range(N)]

print(board)