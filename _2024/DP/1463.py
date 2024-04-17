# 1로 만들기 

import sys
input = sys.stdin.readline

N = int(input())
INF = float("inf")

def find(number): 
    can_make = [ INF for _ in range(number+1) ]
    can_make[number] = 0
    for num in range(number,1,-1):
        if num % 3 == 0:
            if can_make[num] + 1 < can_make[num//3]:
                can_make[num//3] = can_make[num] + 1

        if num % 2 == 0:
            if can_make[num] + 1 < can_make[num//2]:
                can_make[num//2] = can_make[num] + 1

        if can_make[num] + 1 < can_make[num-1]:
            can_make[num-1] = can_make[num] + 1
    return can_make[1]

print(find(N))
    

