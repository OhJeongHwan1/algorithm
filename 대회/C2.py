import sys
import heapq

input = sys.stdin.readline

T = int(input())
answerList = []

for _ in range(T):
    A, B, C = map(int, input().split())
    D = list(map(int, input().split()))

    # 맡긴 외주의 시간을 저장할 최소 힙
    assigned = []
    answer = 0
    lessTime = A
    
    for work in D:
        # 외주를 친구에게 맡길 수 있는 기회가 아직 남아있는 경우
        if len(assigned) < B:
            heapq.heappush(assigned, work)
            helpTime = 0
        # 기회가 남아있지 않지만, 현재 외주의 시간이 맡긴 외주 중 가장 짧은 시간보다 긴 경우
        elif assigned[0] < work:
            helpTime = heapq.heappop(assigned)
            heapq.heappush(assigned, work)
        # 위의 두 경우에 해당하지 않으면 현재 외주를 직접 처리
        else:
            helpTime = work
        
        if lessTime >= helpTime:
            lessTime -= helpTime
            answer += 1
        else:
            break

    answerList.append(answer)

for answer in answerList:
    print(answer)