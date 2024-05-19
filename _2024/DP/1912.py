# 1912 연속합 골 5
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))

for i in range(1,N):
    if numbers[i-1] < 0:
        continue
    if numbers[i] + numbers[i-1] > 0:
        numbers[i] = numbers[i] + numbers[i-1]
print(max(numbers))