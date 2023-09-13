import sys
input = sys.stdin.readline

T = int(input())
scores = []
num_list = []

for i in range(T):
    N = int(input())
    for j in range(N):
        scores.append(list(map(int, input().split())))

    scores.sort()
    min = scores[0][1]
    num = 1
    if min == 1:
        num_list.append(num)
        scores = []
        continue

    for first, second in scores:
        if second > min:
            continue
        elif min > second:
            num += 1
            min = second
    num_list.append(num)
    scores = []

for i in num_list:
    print(i)

