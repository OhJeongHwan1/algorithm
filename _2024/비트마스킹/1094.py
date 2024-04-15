import sys
input = sys.stdin.readline

X = int(input())

bin_x = bin(X)

ans = 0
for i in range(2,len(bin_x)):
    if bin_x[i] == '1':
        ans += 1

print(ans)