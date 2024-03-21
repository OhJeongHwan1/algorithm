import sys
input = sys.stdin.readline

# 순열의 길이
n = int(input()) # 1~20

# n자리로 만들 수 있는 순열의 모든 경우의 수 n!
# 4자리=4!, 3자리=3!
# 자릿수에 따른 순열의 경우의수를 미리 계산한 팩토리얼 리스트
fList = [0] * 21
fList[0] = 1
for i in range(1, n+1):
    # 각 자리수에서 만들 수 있는 경우의수
    fList[i] = fList[i-1] * i

# 숫자 사용여부 리스트
visited = [False] * 21

# 출력 순열 리스트
s = [0] * 21

# 문제종류/순열데이터 입력 리스트
list = list(map(int, input().split()))

if list[0] == 1: # 순열 출력

    k = list[1] # 몇번째 순열을 출력할 지
    for i in range(1, n+1):
        cnt = 1 # 해당 자리에서 몇 번째 숫자를 사용해야 할 지 정하는 변수
        for j in range(1, n+1):
            if visited[j]:  # 이미 사용한 숫자 계산 X
                continue
            if k <= cnt * fList[n-i]: # 맨 앞자리가 몇인 순열에 속하는지
                k -= (cnt-1) * fList[n-i] # k = k- ((cnt-1) * 경우의 수)
                # 현재 자리에 j값 저장
                s[i] = j
                visited[j] = True
                break
            cnt += 1
    # 순열 출력
    for i in range(1, n+1):
        print(s[i], end=" ")

else: # 순열의 순서 출력

    k = 1 # 순열의 순서 저장
    for i in range(1, n+1):
        cnt = 0
        # 현재 자릿수의 숫자보다 앞 숫자 중 미사용 숫자 카운트
        for j in range(1, list[i]):
            if not visited[j]:
                cnt += 1
        # 미사용 숫자 개수 * (현재자리 -1 에서 만들 수 있는 순열의 개수)를 더함
        k += cnt * fList[n-i]
        visited[list[i]] = True

    print(k)