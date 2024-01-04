import sys
input = sys.stdin.readline
N= int(input())
date = [0] * (1001)  # date
d = []                # (과제 점수 : W ) & (남은 일수 : D) 저장
for i in range(N):
    D, W = map(int,input().split())
    d.append((W, D))
d.sort(reverse=True)  # 점수에 대해 내림차순으로 정렬
for i in range(N):
    for j in range(d[i][1], 0, -1): # i부터 시작해서 뒤로 감
        if date[j] == 0:           
            date[j] = d[i][0]
            break
print(sum(date))