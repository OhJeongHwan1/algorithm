# 1966 프린터 큐
# queue 와 인덱스 포인터를 이용한 풀이

import sys
from collections import deque

T = int(input())

result_list = []
for _ in range(T):
    result = 0
    N, M = map(int,input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    m = M
    doc_num = queue[M]

    while queue:
        max_num = max(queue)
        now_num = queue.popleft()
        m -= 1
        
        if now_num == max_num:
            result += 1
            if m < 0:
                result_list.append(result)
                break
        else:
            queue.append(now_num)
            if m < 0:
                m = len(queue) - 1


for result in result_list:
    print(result)