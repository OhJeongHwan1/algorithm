import sys

input = sys.stdin.readline

K = int(input())
M, N = map(int, input().split())
r, c = map(int, input().split())
teldong = [[0 for _ in range(N)] for _ in range(M)]
teldong[r][c] += 1

result = 0
move = [[-1,0],[1,0],[0,-1],[0,1]]


def donsan(r,c,k):
    global result
    if k == -1:
        return
    if r < 0 or r >= M or c < 0 or c >= N:
        result = result + 1
        if result > 1000000007:
            result = result % 1000000007
        return
    k-=1
    donsan(r-1,c,k)
    donsan(r+1,c,k)
    donsan(r,c-1,k)
    donsan(r,c+1,k)

donsan(r,c,K)

print(result)
    
        


