# 11054 가장 긴 바이토닉 부분 수열
# 증가하는 구간과 감소하는 구간을 나누어서 생각해야 함....

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

increase_array = [ 0 for _ in range(N)]
decrease_array = [ 0 for _ in range(N)]
the_length = [ 0 for _ in range(N) ]

for i in range(N):
    if increase_array[i] == 0:
        increase_array[i] = 1

    for j in range(i+1,N):
        if A[i] < A[j]:
            increase_array[j] = max(increase_array[i] + 1,increase_array[j])

for i in range(N-1,-1,-1):    
    if decrease_array[i] == 0:
        decrease_array[i] = 1

    for j in range(i,-1,-1):
        if A[i] < A[j]:
            decrease_array[j] = max(decrease_array[i] + 1,decrease_array[j])

for i in range(N):
    the_length[i] = increase_array[i] + decrease_array[i] - 1

print(max(the_length))