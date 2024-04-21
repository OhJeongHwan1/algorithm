# 전깃줄 - 2 플 5
import sys
input = sys.stdin.readline

N = int(input())
electList = []
LIS = [[-1,0]]
lis_total = [(-1,0)]

def binary_search(LIS,num):
    low = -1
    high = len(LIS)

    while low+1 < high:
        mid = (low+high)//2

        if LIS[mid][0] < num:
            low = mid
        else:
            high = mid

    return high

for _ in range(N):
    electList.append(list(map(int,input().split())))

electList.sort()

new_list = []
for i in range(N):
    new_list.append([electList[i][1],electList[i][0]])

new_list = new_list[::-1]

while new_list:
    B_number, index = new_list.pop()
    
    if B_number > LIS[-1][0]:
        LIS.append([B_number,index])
        lis_total.append((index,len(LIS)-1))
    else:
        find = binary_search(LIS,B_number)

        LIS[find] = [B_number,index]
        lis_total.append((index,find))


ans = len(LIS) - 1
print(N-ans)
ans_list = []
for i in range(N,0,-1):
    if ans == lis_total[i][1]:
        ans_list.append(lis_total[i][0])
        ans -=1
    if ans == 0:
        break

result_list = []

for i in range(N):
    if electList[i][0] not in ans_list:
        result_list.append(electList[i][0])

result_list.sort()

for result in result_list:
    print(result)