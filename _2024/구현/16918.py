# 16918 봄버맨 실1 구현

import sys
input = sys.stdin.readline

R, C, N = map(int,input().split())
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]
board = []
next_bomb = [ [False for _ in range(C)] for _ in range(R)]

for _ in range(R):
    board.append(list(map(str,input().strip())))

def bomb(x,y):

    board[x][y] = '.'

    for dx, dy in MOVE:
        nx,ny = x+dx,y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == 'O':
                board[nx][ny] = '.'

for n in range(1,N+1):
    if n % 2 == 1:
        if n == 1:
            for x in range(R):
                for y in range(C):
                    if board[x][y] == 'O':
                        next_bomb[x][y] = True
                    else:
                        next_bomb[x][y] = False
        else:
            for x in range(R):
                for y in range(C):
                    if next_bomb[x][y] == True:
                        bomb(x,y)

            for x in range(R):
                for y in range(C):
                    if board[x][y] == 'O':
                        next_bomb[x][y] = True
                    else:
                        next_bomb[x][y] = False

    else:
        for x in range(R):
            for y in range(C):
                if board[x][y] == '.':
                    board[x][y] = 'O'


for x in range(R):
    for y in range(C):
        print(board[x][y],end='')
    print()