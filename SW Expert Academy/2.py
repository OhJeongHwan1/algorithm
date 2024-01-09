def solve(i, j, k):
    global drop

    # lst[i][0] + lst[j][1] + lst[k][2]

    # 소멸되어야 할 최소 능력
    r1 = sum(lst[i]) - lst[i][0]
    r2 = sum(lst[j]) - lst[j][1]
    r3 = sum(lst[k]) - lst[k][2]

    if drop > r1+r2+r3:
        drop = r1+r2+r3
        r.clear()
        r.append(i)
        r.append(j)
        r.append(k)

def cal():
    global lost

    for i in range(N):
        if i not in r:
            lost += (sum(lst[i]) - max(lst[i]))


T = int(input())


for t in range(1, T+1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    if N < 3:
        result = -1

    else:
        drop = float('inf')
        lost = 0
        r = []

        for i in range(N):
            for j in range(i+1, N):
                for k in range(i+2, N):
                    solve(i, j, k)


        cal()
        result = lost + drop

    print(f"#{t} {result}")