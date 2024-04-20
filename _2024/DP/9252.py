# 9252 LCS2 골5
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
ans_list = []

x, y = length1, length2
while True:
    cnt = 0
    for dx,dy in [[-1,0],[0,-1]]:
        nx,ny = x+dx,y+dy

        if dp[nx][ny] == dp[x][y]:
            x,y = nx,ny
            cnt +=1

    if cnt == 0:
        ans_list.append(first_word[x-1])
        ans -=1
        x,y = x-1,y-1

    if ans == 0:
        break

ans_list = ans_list[::-1]

for word in ans_list:
    print(word,end='')

    

