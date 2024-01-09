import sys

input = sys.stdin.readline

global road
road = [sys.maxsize for _ in range(10001)]

def find_locate(num):
    locate = 1
    while True:
        num = num-locate

        if num <= 0:
            break

        locate +=1

    return locate

def reset_road_array():
    global road
    road = [sys.maxsize for _ in range(10001)]

def check_first(num):
    locate = 0
    while num > 0:
        num = num-locate

        if num == 1:
            return True

        locate +=1

    return False

def check_last(num):
    locate = 1
    while num > 0:
        num = num-locate

        if num == 0:
            return True

        locate +=1

    return False


def dp(origin,goal):
    if origin == goal:
        return
    if find_locate(origin) == find_locate(goal):
        if road[goal] > road[origin] + abs(origin-goal):
            road[goal] = road[origin] + abs(origin-goal)
        return
    else:
        if origin < goal:
            if origin+find_locate(origin) > 10000 or origin+find_locate(origin) +1 > 10000:
                return
            if road[origin+find_locate(origin)] > road[origin] + 1:
                road[origin+find_locate(origin)] = road[origin] + 1
                dp(origin+find_locate(origin),goal)

            if road[origin+find_locate(origin)+1] > road[origin] + 1:
                road[origin+find_locate(origin)+1] = road[origin] + 1
                dp(origin+find_locate(origin)+1,goal)
        if origin > goal:
            if check_first(origin) == False and check_last(origin) == False:
                if road[origin-find_locate(origin)] > road[origin] + 1:
                    road[origin-find_locate(origin)] = road[origin] + 1
                    dp(origin-find_locate(origin)+1,goal)
                if road[origin-find_locate(origin)+1] > road[origin] + 1:
                    road[origin-find_locate(origin)+1] = road[origin] + 1
                    dp(origin-find_locate(origin),goal)
            if check_first(origin) == True:
                if  road[origin-find_locate(origin)+1] > road[origin] + 1:
                    road[origin-find_locate(origin)+1] = road[origin] + 1
                    dp(origin-find_locate(origin)+1,goal)
            if check_last(origin) == True:
                if road[origin-find_locate(origin)] > road[origin] + 1:
                    road[origin-find_locate(origin)] = road[origin] + 1
                    dp(origin-find_locate(origin),goal)


T = int(input())

test_list = []

for i in range(T):
    test_list.append(list(map(int,input().split())))

count = 1

for test in test_list:
    road[test[0]] = 0

    if test[0] == test[1]:
        print("#"+str(count),end=' ')
        print(0)
        continue

    dp(test[0],test[1])

    print("#"+str(count),end=' ')
    print(road[test[1]])

    reset_road_array()

    count += 1