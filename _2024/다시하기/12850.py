# 12850 본대 산책 2 골1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

D = int(input())
# 정보 과학관 1, 전산관 2, 미래관 3, 신양관 4, 한경직 기념관 5
# 진리관 6, 학생회관 7, 형남 공학관 8
ans = 0

sungsil = [[] for _ in range(9)]
sungsil[1].extend([2,3])
sungsil[2].extend([1,3,4])
sungsil[3].extend([1,2,4,5])
sungsil[4].extend([2,3,5,6])
sungsil[5].extend([3,4,6,8])
sungsil[6].extend([4,5,7])
sungsil[7].extend([6,8])
sungsil[8].extend([5,7])

def solve(now,cnt):
    global ans 
    if cnt == 0:
        ans += 1
        return

    for next in sungsil[now]:
        solve(next,cnt-1)

solve(1,D)
print(ans%1000000007)
