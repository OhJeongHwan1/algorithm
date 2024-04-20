# 14003 가장 긴 증가하는 부분 수열 5
# 이분 탐색을 이용한 LIS 문제
# 출처 https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 다시 보기

import sys
input = sys.stdin.readline

def binary_search(lis_arr, num): 
    low = -1 
    high = len(lis_arr) 

    while low +1 < high:
       
        mid = (low + high)//2 

        if num > lis_arr[mid]: 
            low = mid
        else:
            high = mid

    return high

N = int(input())

num_array = list(map(int, sys.stdin.readline().split()))
lis_arr = [-1000000001]
lis_total = [(-1000000001,0)]

num_array = num_array[::-1]

while num_array:
    number = num_array.pop()

    if number > lis_arr[-1]:
        lis_arr.append(number)
        lis_total.append((number,len(lis_arr)-1))
    else:
        index = binary_search(lis_arr, number)
        lis_arr[index] = number
        lis_total.append((number,index))

ans = len(lis_arr)-1
print(ans)
ans_list = []
for i in range(N,0,-1):
    if ans == lis_total[i][1]:
        ans_list.append(lis_total[i][0])
        ans -=1
    if ans == 0:
        break

ans_list.sort()
print(*ans_list)