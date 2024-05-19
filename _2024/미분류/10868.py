# 최솟값 골1
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

numbers = [int(input()) for _ in range(N)]
the_range = [list(map(int,input().split())) for _ in range(M)]

for i in range(M):
    new_numbers = numbers[the_range[i][0]-1:the_range[i][1]]

    