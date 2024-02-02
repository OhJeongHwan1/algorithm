# 1747 팬린드롬 소수

import sys

input = sys.stdin.readline

N = int(input())

def checkDemical(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
            
def checkFellin(num):
    num_list = list(map(int,str(num)))
    
    for i in range(len(num_list)//2):
        if num_list[i] != num_list[-(i+1)]:
            return False
        
    return True

find_number = N  

while True:

    if checkFellin(find_number) == True:
        if checkDemical(find_number) == True:
            print(find_number)
            break

    find_number += 1

    
