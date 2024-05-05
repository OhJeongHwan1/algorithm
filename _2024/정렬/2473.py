# 2473 세 용액 골3
# 정렬
import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int,input().split()))
MIN = 3000000001
result_list = []
liquids.sort()

for i in range(N-1):
    standard = liquids[i]
    start = i+1
    end = N-1
    
    while start < end:
        total = liquids[start] + liquids[end] + standard
        if abs(total) < MIN:
            result_list = [liquids[start],liquids[end],standard]
            MIN = abs(total)

        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            result_list = [liquids[start],liquids[end],standard]
            break

result_list.sort()

print(*result_list)

        
