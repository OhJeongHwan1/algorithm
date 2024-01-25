# 스택을 사용한 풀이 방법

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
origin_number = list(input().strip())

# 스택 초기화
stack = []

# K개의 숫자를 제거해야 함
for num in origin_number:
    # 스택이 비어있지 않고, 제거할 숫자가 남아있으며,
    # 스택의 마지막 숫자가 현재 숫자보다 작은 경우 스택에서 제거
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1

    # 현재 숫자를 스택에 추가
    stack.append(num)

# K가 여전히 남아있다면, 스택의 끝에서 K개의 숫자를 제거
if K > 0:
    stack = stack[:-K]

# 결과 출력
print(''.join(stack))
