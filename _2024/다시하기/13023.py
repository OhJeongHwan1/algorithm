# 감소하는 수 골5
# 백트래킹
# 진짜 상상도 못한 풀이 ㄴㅇㄱ
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
answer = []

for i in range(1,11):
    for comb in combinations(range(10),i):
        number = sorted(list(comb),reverse=True)
        answer.append(int("".join(map(str,number))))
answer.sort()

if N >= len(answer):
    print(-1)
else:
    print(answer[N])
    