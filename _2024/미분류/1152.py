# 1152 단어의 개수 브 2
import sys
input = sys.stdin.readline

words = list(map(str,input().strip().split(' ')))
new_words = []
for word in words:
    if word != '':
        new_words.append(word)

print(len(new_words))