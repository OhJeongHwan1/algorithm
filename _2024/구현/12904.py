# 12904 A와B 구현

import sys
input = sys.stdin.readline

S = input().strip()
T = list(map(str,input().strip()))
t = T

while len(list(map(str,S))) != len(t):
    if t[-1] == 'A':
        t.pop()
        continue
    if t[-1] == 'B':
        t.pop()
        t = t[::-1]
        continue

word = ''

for alp in t:
    word += alp

if S == word:
    print(1)
else:
    print(0)