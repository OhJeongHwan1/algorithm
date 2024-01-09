import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 # 초기 값


for i in range(n):
    for j in range(n):

        #  맨 끝 점이면 탈출.
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        # 오른쪽으로
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]

        # 아래로
        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]
