# 5212 지구 온난화 실2
import sys
input = sys.stdin.readline

R,C = map(int, input().split())
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]
the_map = [] 

for _ in range(R):
    the_map.append(list(map(str,input().strip())))

def check_disapear(x,y):
    count = 0
    for dx, dy in MOVE:
        nx,ny = x+dx,y+dy
        if 0 <= nx < len(the_map) and 0 <= ny < len(the_map[0]):
            if the_map[nx][ny] == '.':
                count += 1
        else:
            count += 1
    if count >= 3:
        return True
    
    return False

def change_map():
    check_min_x = len(the_map)
    check_min_y = len(the_map[0])
    check_max_x = 0
    check_max_y = 0

    for x in range(len(the_map)):
        for y in range(len(the_map[0])):
            if the_map[x][y] =='X':
                if x < check_min_x:
                    check_min_x = x
                if x > check_max_x:
                    check_max_x = x
                if y < check_min_y:
                    check_min_y = y
                if y > check_max_y:
                    check_max_y = y

    new_map_x = check_max_x-check_min_x+1
    new_map_y = check_max_y-check_min_y+1

    new_map = [ [0 for _ in range(new_map_y)] for _ in range(new_map_x)]

    for x in range(new_map_x):
        for y in range(new_map_y):

            new_map[x][y] = the_map[x+check_min_x][y+check_min_y]
    return new_map

for x in range(len(the_map)):
    for y in range(len(the_map[0])):
        if the_map[x][y] == 'X':
            if check_disapear(x,y) == True:
                the_map[x][y] = 'Y'

for x in range(len(the_map)):
    for y in range(len(the_map[0])):
        if the_map[x][y] == 'Y':
            the_map[x][y] = '.'
    
the_map = change_map()

for x in range(len(the_map)):
    for y in range(len(the_map[0])):
        print(the_map[x][y],end='')
    print()