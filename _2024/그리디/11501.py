# 11501 주식 실2
import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    ans = 0
    the_max = 0 
    
    for i in range(N-1,-1,-1):
        if the_max < price[i]:
            the_max = price[i]
        ans += the_max - price[i]

    print(ans)