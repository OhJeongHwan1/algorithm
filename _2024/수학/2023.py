# 2023 신기한 소수

import sys

input = sys.stdin.readline

N = int(input())

num_list = [2,3,5,7]

def checkDemical(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

remain_len = N

while remain_len > 1:
    new_num_list = []

    for num in num_list:
        for i in range(1,10,2):
            new_num = num*10 + i  
            if checkDemical(new_num) == True:
                new_num_list.append(new_num)

    num_list = new_num_list
    remain_len -= 1

for num in num_list:
    print(num)