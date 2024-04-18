# 2263 트리의 순회 골 2
# 전위 순회 중위 순회 후위 순회 공부

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

idx_map = {value: idx for idx, value in enumerate(inorder)}
    
# 전위 순회 결과를 출력하는 재귀 함수
def recursive(left, right, post_end):
    if left > right:
        return
        
    # 후위 순회의 마지막 원소는 현재 서브트리의 루트
    root = postorder[post_end]
    print(root, end=' ')
        
    # 루트의 인덱스를 중위 순회에서 찾기
    idx = idx_map[root]
        
    # 왼쪽 서브트리 순회
    recursive(left, idx - 1, post_end - (right - idx) - 1)
        
    # 오른쪽 서브트리 순회
    recursive(idx + 1, right, post_end - 1)
    
    # 전체 트리에 대해 함수 실행
recursive(0, len(inorder) - 1, len(postorder) - 1)