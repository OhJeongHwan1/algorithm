# 골5 하노이탑 재귀
# 하노이탑의 동작 원리를 재귀로 잘 구현하는 것이 중요하다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

K = int(input())

def top(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        top(n-1, a, c, b) 
        print(a, c)
        top(n-1, b, a, c)
sum = 2 ** K - 1
print(sum)

top(K, 1, 2, 3)