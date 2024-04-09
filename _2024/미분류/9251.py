# 9251 LCS 골5
import sys
input = sys.stdin.readline

first_word = list(input().strip())
second_word = list(input().strip())

f_pointer = 0
s_pointer = 0
result = 0

while f_pointer < len(first_word) and s_pointer < len(second_word):

    if first_word[f_pointer] == second_word[s_pointer]:
        f_pointer += 1
        s_pointer += 1
        result += 1
    else:
        if s_pointer <= f_pointer:
            s_pointer += 1
        else:
            f_pointer += 1

print(result)