# 2239 스도쿠

import sys
input = sys.stdin.readline

sudocu = []

for _ in range(9):
    sudocu.append(list(input().strip()))

def check_column_row(num,x,y):
    if str(num) in sudocu[x]:
        return True
    for i in range(9):
        if str(num) == sudocu[i][y]:
            return True
    
    return False

def check_box(num,x,y):
    find_x = x % 3
    find_y = y % 3

    if find_x == 0 and find_y == 0:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 0 and find_y == 1:
        for i in range(x,x+3):
            for j in range(y-1,y+2):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 1 and find_y == 0:
        for i in range(x-1,x+2):
            for j in range(y,y+3):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 1 and find_y == 1:
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 2 and find_y == 1:
        for i in range(x-2,x+1):
            for j in range(y-1,y+2):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 1 and find_y == 2:
        for i in range(x-1,x+2):
            for j in range(y-2,y+1):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 2 and find_y == 2:
        for i in range(x-2,x+1):
            for j in range(y-2,y+1):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 0 and find_y == 2:
        for i in range(x,x+3):
            for j in range(y-2,y+1):
                if str(num) == sudocu[i][j]:
                    return True
                
    if find_x == 2 and find_y == 0:
        for i in range(x-2,x+1):
            for j in range(y,y+3):
                if str(num) == sudocu[i][j]:
                    return True
                
    return False

for x in range(9):
        for y in range(9):
            if sudocu[x][y] == '0':
                the_list = []
                for i in range(1,10):
                        if check_box(i,x,y) == False and check_column_row(i,x,y) == False:
                            the_list.append(str(i))
                
                if len(the_list) == 1:
                    sudocu[x][y] = the_list[0]

                else:
                    sudocu[x][y] = the_list

while True:
    for x in range(9):
        for y in range(9):
            if type(sudocu[x][y]) == list:
                the_list = []
                for candidate in sudocu[x][y]:
                    if check_box(candidate,x,y) == False and check_column_row(candidate,x,y) == False:
                            the_list.append(candidate)

                if len(the_list) == 1:
                    sudocu[x][y] = the_list[0]

                else:
                    sudocu[x][y] = the_list

    count = 0
    for x in range(9):
        for y in range(9):
            if type(sudocu[x][y]) == list:
                count += 1
                break
    
    if count == 0:

        for line in sudocu:
            for number in line:
                print(number,end='')
            print()
        break


