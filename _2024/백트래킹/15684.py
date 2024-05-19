# 15684 사다리 조작
import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())
ans = 0
lines = [list(map(int,input().split())) for _ in range(M)]

if M == 0:
    print(0)
else:
    print(ans)