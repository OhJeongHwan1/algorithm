# 로또 6603 실2
# 조합

import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    the_input = list(map(int,input().split()))
    if the_input[0] == 0:
        break
    K, S = the_input[0], the_input[1:]
    
    for the_list in combinations(S,6):
        print(*the_list)

    print()
