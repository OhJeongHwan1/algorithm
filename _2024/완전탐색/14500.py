# 테트로미노

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

the_paper = [list(map(int,input().split())) for _ in range(N)]
result = 0

def the_one():
    global result

    for i in range(N-3):
        for j in range(M):
            num = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+2][j] + the_paper[i+3][j]
            if num > result:
                result = num

    for i in range(N):
        for j in range(M-3):
            num = the_paper[i][j] + the_paper[i][j+1] + the_paper[i][j+2] + the_paper[i][j+3]
            if num > result:
                result = num

def the_two():
    global result

    for i in range(N-1):
        for j in range(M-1):
            num = the_paper[i][j] + the_paper[i+1][j] + the_paper[i][j+1] + the_paper[i+1][j+1]
            if num > result:
                result = num

def the_three():
    global result

    for i in range(N-2):
        for j in range(M-1):
            num_1 = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+2][j] + the_paper[i][j+1]
            num_2 = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+2][j] + the_paper[i+2][j+1]
            num_3 = the_paper[i][j] + the_paper[i][j+1] + the_paper[i+1][j+1] + the_paper[i+2][j+1]
            num_4 = the_paper[i+2][j] + the_paper[i][j+1] + the_paper[i+1][j+1] + the_paper[i+2][j+1]
            if max(num_1,num_2,num_3,num_4) > result:
                result = max(num_1,num_2,num_3,num_4)

    for i in range(N-1):
        for j in range(M-2):
            num_1 = the_paper[i][j] + the_paper[i][j+1] + the_paper[i][j+2] + the_paper[i+1][j]
            num_2 = the_paper[i][j] + the_paper[i][j+1] + the_paper[i][j+2] + the_paper[i+1][j+2]
            num_3 = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+1][j+1] + the_paper[i+1][j+2]
            num_4 = the_paper[i][j+2] + the_paper[i+1][j] + the_paper[i+1][j+1] + the_paper[i+1][j+2]
            if max(num_1,num_2,num_3,num_4) > result:
                result = max(num_1,num_2,num_3,num_4)


def the_four():
    global result

    for i in range(N-2):
        for j in range(M-1):
            num_1 = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+1][j+1] + the_paper[i+2][j+1]
            num_2 = the_paper[i][j+1] + the_paper[i+1][j] + the_paper[i+1][j+1] + the_paper[i+2][j]
            if max(num_1,num_2) > result:
                result = max(num_1,num_2)


    for i in range(N-1):
        for j in range(M-2):
            num_1 = the_paper[i][j] + the_paper[i][j+1] + the_paper[i+1][j+1] + the_paper[i+1][j+2]
            num_2 = the_paper[i+1][j] + the_paper[i][j+1] + the_paper[i+1][j+1] + the_paper[i][j+2]
            if max(num_1,num_2) > result:
                result = max(num_1,num_2)

def the_five():
    global result

    for i in range(N-2):
        for j in range(M-1):
            num_1 = the_paper[i][j] + the_paper[i+1][j] + the_paper[i+2][j] + the_paper[i+1][j+1]
            num_2 = the_paper[i][j+1] + the_paper[i+1][j] + the_paper[i+2][j+1] + the_paper[i+1][j+1]
            if max(num_1,num_2) > result:
                result = max(num_1,num_2)

    for i in range(N-1):
        for j in range(M-2):
            num_1 = the_paper[i][j] + the_paper[i][j+1] + the_paper[i][j+2] + the_paper[i+1][j+1]
            num_2 = the_paper[i+1][j] + the_paper[i][j+1] + the_paper[i+1][j+2] + the_paper[i+1][j+1]
            if max(num_1,num_2) > result:
                result = max(num_1,num_2)

the_one()
the_two()
the_three()
the_four()
the_five()

print(result)