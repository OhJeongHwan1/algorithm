import sys
input = sys.stdin.readline

M = int(input())

S = [ 0 for _ in range(20+1)]
ans = []
for _ in range(M):
    sik = input()
    if 'all' in sik or 'empty' in sik:
        operator = sik.strip()
    else:
        operator, num = sik.split()

    if operator == 'add':
        S[int(num)] = 1
    if operator == 'check':
        if S[int(num)] == 1:
            print(1)
        else:
            print(0)
    if operator == 'remove':
        S[int(num)] = 0
    if operator == 'toggle':
        S[int(num)] = 0 if S[int(num)] == 1 else 1
    if operator == 'all':
        for i in range(1,21):
            S[i] = 1
    if operator == 'empty':
        for i in range(1,21):
            S[i] = 0

