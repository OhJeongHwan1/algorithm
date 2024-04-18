# 2143 두 배열의 합 골 2?
# 이러한 방식으로 누적합을 구할 필요가 있다는사실을 알아야함.
import sys
import bisect
input = sys.stdin.readline

T = int(input())
ans = 0
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

aan, bbn = [], []
for i in range(n):
    for j in range(i+1, n+1):
        aan.append(sum(a[i:j]))

for i in range(m):
    for j in range(i + 1, m + 1):
        bbn.append(sum(b[i:j]))
aan.sort()
bbn.sort()

for i in range(len(aan)):
    left = bisect.bisect_left(bbn,T - aan[i])
    right = bisect.bisect_right(bbn,T - aan[i])
    ans += (right-left)

print(ans)
