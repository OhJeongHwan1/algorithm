# 10986 나머지 합
# 누적합과 조합을 사용해야 하는 문제임. 어려움.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * M # m으로 나눈 나머지 담는 곳
prefixSum = 0
for i in range(N):
    prefixSum += a[i]
    r[prefixSum % M] += 1

ans = r[0] # 나머지가 0이 되는 경우의 수

for i in range(M):
    # nC2 = n(n-1)/2
    ans += r[i] * (r[i]-1) // 2
print(ans)



