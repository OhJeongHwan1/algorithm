import sys

n = int(sys.stdin.readline().rstrip())

alls = []
do = [False] *1001

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    alls.append([d, w])

alls.sort(reverse =True)
print(alls)
score = 0

for d, w in alls:
    i = d
    while i > 0 and do[i]:
        i -= 1
    if i == 0:
        continue
    else:
        do[i] = True
        score += w
print(score)