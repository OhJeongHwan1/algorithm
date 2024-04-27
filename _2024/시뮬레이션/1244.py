# 1244 스위치 켜고 끄기 실 4
# 시뮬레이션

N = int(input())
start = list(map(int,input().split()))
S = int(input())

for _ in range(S):
    gender, switch = map(int,input().split())

    if gender == 1:
        for i in range(switch-1,N,switch):
            start[i] = 1 if start[i] == 0 else 0

    else:
        now = switch - 1
        start[now] = 1 if start[now] == 0 else 0
        for i in range(N//2):
            if 0 <= now - i and now + i < N:
                if start[now+i] == start[now-i]:
                    start[now+i] = 1 if start[now+i] == 0 else 0
                    start[now-i] = 1 if start[now-i] == 0 else 0
                else:
                    break
            else:
                break


for i in range(N):
    if i % 20 == 0 and i != 0:
        print()
    print(start[i],end=' ')
    