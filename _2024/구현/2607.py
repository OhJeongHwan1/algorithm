# 2607 비슷한 단어 실2
# 간단한 노가다 구현 문제

import sys
input = sys.stdin.readline

N = int(input())
origin_word = list(map(str,input().strip()))
other_words = []
result = 0

for _ in range(N-1):
    other_words.append(list(map(str,input().strip())))

for other_word in other_words:
    copy_word = origin_word.copy()

    if len(other_word) - 1 <= len(copy_word) <= len(other_word) + 1:
        if len(other_word) == len(copy_word):
            for alp in other_word:
                for i in range(len(copy_word)):
                    if alp == copy_word[i]:
                        copy_word.pop(i)
                        break
            if len(copy_word) == 0 or len(copy_word) == 1:
                # print(other_word)
                result += 1

        elif len(other_word) < len(copy_word):
            for alp in other_word:
                for i in range(len(copy_word)):
                    if alp == copy_word[i]:
                        copy_word.pop(i)
                        break
            if len(copy_word) == 1:
                # print(other_word)
                result += 1

        elif len(other_word) > len(copy_word):
            for alp in other_word:
                for i in range(len(copy_word)):
                    if alp == copy_word[i]:
                        copy_word.pop(i)
                        break
            if len(copy_word) == 0:
                # print(other_word)
                result += 1

print(result)


