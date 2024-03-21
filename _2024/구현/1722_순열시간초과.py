# 1722 순열의 순서 구현
# 순열을 이용한 문제일 줄 알았으나 당연히 메모리 초과
# 수학적 접근이 필요했음
# 질 좋은 문제

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
k = list(map(int,input().split()))
number = [ i+1 for i in range(N) ]

if k[0] == 1:
    index = 0

    for the_list in permutations(number,N):
        index += 1
        list = []

        for alp in the_list:
            list.append(alp)
        
        if index == k[1]:
            print(*list)
            break

if k[0] == 2:

    k = k[1:]
    index = 0

    for the_list in permutations(number,N):
        index += 1
        list = []
        for alp in the_list:
            list.append(alp)

        if list == k:
            print(index)
            break
