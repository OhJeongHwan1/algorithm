N = int(input())
num = sorted([int(input()) for _ in range(N)])
re_num = []

# B-A, C-B, D-C... 쭉 구해서 새 리스트에 추가
for i in range(1, N):
    re_num.append(num[i] - num[i-1])

# 두 수의 최대공약수를 구해주는 함수(유클리드 호제법)
def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

# re_num의 모든 수들의 최대공약수를 구하고 그 것의 1을 제외한 모든 약수가 구하는 M이다.
GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[idx])

result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))