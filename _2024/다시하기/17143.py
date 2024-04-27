# 17143 낚시왕
import sys
input = sys.stdin.readline
R, C, M = map(int,input().split())

fishing_map = [[-1 for _ in range(C+1)] for _ in range(R+1)]
sharks = [list(map(int,input().split())) for _ in range(M)]



