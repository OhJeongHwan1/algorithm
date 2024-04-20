# 9251 LCS 골5
import sys
input = sys.stdin.readline

first_word = list(input().strip())
second_word = list(input().strip())
length1 = len(first_word)
length2 = len(second_word)

dp = [[0 for _ in range(length2+1)] for _ in range(length1+1)]

for i in range(1,length1+1):
    for j in range(1,length2+1):
        if first_word[i-1] == second_word[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = dp[length1][length2]
print(ans)
