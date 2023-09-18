def canChange(start, target):
    # G와 F의 위치를 구합니다.
    g_pos_start = [i for i, x in enumerate(start) if x == 'G']  #함수의 인덱스의 인덱스값을 알려주는 enumerate 함수 
    g_pos_target = [i for i, x in enumerate(target) if x == 'G']
    f_pos_start = [i for i, x in enumerate(start) if x == 'F']
    f_pos_target = [i for i, x in enumerate(target) if x == 'F']

    if len(g_pos_start) != len(g_pos_target) or len(f_pos_start) != len(f_pos_target):
        return False

    # G의 이동을 확인합니다.
    for s, t in zip(g_pos_start, g_pos_target): #튜플 형태로 2개의 list를 묶어주는 함수
        if s < t:  # G는 왼쪽으로만 이동할 수 있습니다.
            return False
        for i in range(t, s):  # 이동하는 동안 다른 돌이 있는지 확인합니다.
            if start[i] != 'O':
                return False

    # F의 이동을 확인합니다.
    for s, t in zip(f_pos_start, f_pos_target):
        if s > t:  # F는 오른쪽으로만 이동할 수 있습니다.
            return False
        for i in range(s + 1, t + 1):  # 이동하는 동안 다른 돌이 있는지 확인합니다.
            if start[i] != 'O':
                return False

    return True

# 입력 예제
N = int(input())
start = input().strip()
target = input().strip()

# 결과 출력
print("true" if canChange(start, target) else "false")

