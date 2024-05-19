# 1233 주사위 브2
import sys
input = sys.stdin.readline

s1,s2,s3 = map(int,input().split())
sum = s1+s2+s3
result = [0 for _ in range(sum+1)]

for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            result[i+j+k] += 1

max = max(result)

for i in range(1,sum+1):
    if max == result[i]:
        print(i)
        break