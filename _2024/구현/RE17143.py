# 17143 낚시왕
# 다음에 다시 도전..
# 상어의 속도와 방향을 이용하여 다음 속도와 방향을 구하는 관계식 필요

import sys

input = sys.stdin.readline

R, C, M = map(int,input().split())

sharks = []
fishing_map = [[-1 for _ in range(C+1)] for _ in range(R+1)]
total_size = 0

for _ in range(M):
    sharks.append(list(map(int,input().split())))

for i in range(M):
    x,y,speed,direction,size = sharks[i]
    fishing_map[x][y] = i

for fisher_man in range(1,C+1):
    for i in range(1,R+1):
        if fishing_map[i,fisher_man] != -1:
            fishing_map[i,fisher_man] = -1
            total_size += sharks[fishing_map[i,fisher_man]][2]
            break
    
    for i in range(1,R+1):
        for j in range(1,C+1):
            if fishing_map[i,j] == -1:
                x,y,speed,direction,size = sharks[fishing_map[i,j]]

                if direction == 1:
                    x-speed
                    print("위로")

                if direction == 2:
                    print("아래로")
                     
                if direction == 3:
                    print("오른쪽으로")

                if direction == 4:
                    print("왼쪽으로")
                    


print(sharks)
print(fishing_map)
