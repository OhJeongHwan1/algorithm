# 2981 검문
# 이 코드는 숫자의 크기가 10억까지 이기 떄문에 for 문으로 해결할 수 없음.
# 그렇기 때문에 수학적 지식으로 해결해야 함.

import sys

input = sys.stdin.readline

N = int(input())
number_list = []

for _ in range(N):
    number_list.append(int(input()))

standard_num = number_list[0]
result_list = []

for i in range(2,standard_num+1):
    remain = -1

    for j in range(len(number_list)):
        if remain == -1:
            remain = number_list[j] % i
        else:
            if remain != number_list[j] % i:
                break 

            if j == len(number_list) - 1:
                result_list.append(i)

print(*result_list)

            
    

    