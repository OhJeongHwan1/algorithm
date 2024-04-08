#2096 내려가기 골 5
# 슬라이딩 윈도우 
# 메모리 초과를 방지하기 위하여

import sys
input = sys.stdin.readline
N = int(input())
the_list = list(map(int,input().split()))

max_dp = the_list
min_dp = the_list

for _ in range(N-1):
    the_list = list(map(int,input().split()))

    max_dp = [the_list[0] + max(max_dp[0],max_dp[1]),the_list[1] + max(max_dp), the_list[2] + max(max_dp[1],max_dp[2])]
    min_dp = [the_list[0] + min(min_dp[0],min_dp[1]),the_list[1] + min(min_dp), the_list[2] + min(min_dp[1],min_dp[2])]


print(max(max_dp), min(min_dp))