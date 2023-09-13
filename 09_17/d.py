MOD = 1000000007

# 전역 변수로 선언
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_valid(r, c):
    return 0 <= r < M and 0 <= c < N

def dp(r, c, k):
    if teldong[r][c][k] != -1:
        return teldong[r][c][k]

    teldong[r][c][k] = 0
    if k == 0:
        return teldong[r][c][k]

    for d in move:
        next_r, next_c = r + d[0], c + d[1]
        if not is_valid(next_r, next_c):
            continue
        teldong[r][c][k] = (teldong[r][c][k] + dp(next_r, next_c, k - 1)) % MOD
    
    return teldong[r][c][k]

K = int(input())
M, N = map(int, input().split())
r, c = map(int, input().split())

# 3차원 DP 배열 초기화
teldong = [[[-1] * (K + 1) for _ in range(N)] for _ in range(M)]
teldong[r][c][0] = 1

result = 0
for k in range(K):
    for i in range(M):
        result = (result + dp(i, 0, k) + dp(i, N - 1, k)) % MOD
    for j in range(N):
        result = (result + dp(0, j, k) + dp(M - 1, j, k)) % MOD

print(result)
