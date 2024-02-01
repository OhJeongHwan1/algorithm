# 1747 팬린드롬 소수

import sys

input = sys.stdin.readline

N = int(input())

def checkDemical(num):
    if num !=2 and num%2 ==0:
        return False
    
    if num == 2:
        return True
    
    for i in range(3,num+1,2):
        if num % i == 0:
            if i == num:
                return True
            else:
                return False
            
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

    
