# 14002 가장 긴 증가하는 부분 수열 4

import sys
N = int(input())

num_array = list(map(int, sys.stdin.readline().split()))

dp = [1 for i in range(N)]
before_list = [ -1 for i in range(N) ]
result_list = []

for i in range(N):
    for j in range(i,N):
        if num_array[i] < num_array[j]:
            if dp[j] < dp[i]+1:
                dp[j] += 1
                before_list[j] = i

print(max(dp))
index = 0
for i in range(N):
    if dp[i] == max(dp):
        index = i
        break

while index != -1:
    result_list.append(num_array[index])
    index = before_list[index]

result_list.sort()

print(*result_list)