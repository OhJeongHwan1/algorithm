import sys

n = int(sys.stdin.readline())
cnn = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def divide(size, x, y):
    mid=size//2
    if size==2:
        answer=[cnn[x][y], cnn[x+1][y], cnn[x][y+1], cnn[x+1][y+1]]
        answer.sort(reverse=True)
        return answer[1]
    lt=divide(mid, x, y)
    rt=divide(mid, x+mid, y)
    lb=divide(mid, x, y+mid)
    rb=divide(mid, x+mid, y+mid)
    answer=[lt, rt, lb, rb]
    answer.sort(reverse=True)
    return answer[1]
print(divide(n, 0, 0))