# 2812 크게 만들기
# 스택을 사용하여 시간을 단축 시킬 수 있음.

import sys

input = sys.stdin.readline

N, K = map(int,input().split())

origin_number = list(input().strip())

erase = K
start = 0

while erase > 0:
    max = -1
    max_index = 0

    if erase == N-start:
        for i in range(start,start+erase):
            origin_number[i] = -1
        break

    for i in range(start,start+erase+1):
        #print(start,erase,i)
        if int(origin_number[i]) > max:
            max = int(origin_number[i])
            max_index = i

        if max == 9:
            break

    #print(max_index)

    for i in range(start,max_index):
        if int(origin_number[i]) < max:
            origin_number[i] = -1
            erase = erase - 1

    start = max_index + 1

for num in origin_number:
    if num != -1:
        print(num,end='')