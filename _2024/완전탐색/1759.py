# 1759 암호 만들기
# 조합 itertools 사용

import sys
from itertools import combinations

input = sys.stdin.readline

GATHERS = ['a','e','i','o','u']
L, C = map(int,input().split())
alphabets = list(map(str,input().split()))
words = []

alphabets.sort()

for combi in combinations(alphabets,L):

    gather_number = 0

    for check in combi:
        if check in GATHERS:
            gather_number += 1

    if 1 <= gather_number <= L - 2:
        word = ''
        for alp in combi:
            word += alp
        words.append(word)

for word in words:
    print(word)