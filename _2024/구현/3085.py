# 3085 사탕게임

import sys
input = sys.stdin.readline

N = int(input())

board = [ list(map(str,input().strip())) for _ in range(N) ]
bomboni = 0

def change(x,y):
    result = 0

    for dx, dy in ([1,0],[0,1]):
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < N:
            if board[x][y] != board[nx][ny]:
                board[x][y],board[nx][ny] = board[nx][ny],board[x][y]
                result = max(check(x,y),check(nx,ny),result)
                board[x][y],board[nx][ny] = board[nx][ny],board[x][y]
    return result

def check(x,y):

    number1 = 1
    for i in range(1,N-x):
        if board[x][y] == board[x+i][y]:
            number1 += 1
        else:
            break

    for i in range(1,x+1):
        if board[x][y] == board[x-i][y]:
            number1 += 1
        else:
            break

    number2 = 1
    for i in range(1,N-y):
        if board[x][y] == board[x][y+i]:
            number2 += 1
        else:
            break

    for i in range(1,y+1):
        if board[x][y] == board[x][y-i]:
            number2 += 1
        else:
            break

    return max(number1,number2)


for i in range(N):
    for j in range(N):
        if bomboni < check(i,j):
            bomboni = check(i,j)

for i in range(N):
    for j in range(N):
        if bomboni < change(i,j):
            bomboni = change(i,j)


print(bomboni)