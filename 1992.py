n = int(input())

tree = [list(map(int,(input()))) for _ in range(n)]
result = [] # 배열을 생성해서 여기로 넣는다. 

def quad_tree(x,y,n):
    global result
    color = tree[x][y]
    if n == 1: # 크기가 1인 경우 바로 넣고 반환
        result.append(color)
        return
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]:
                result.append("(")  # 시작과 끝에 () 추가
                quad_tree(x,y,n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color) 

quad_tree(0,0,n)
print("".join(map(str,(result))))

## 쿼드 트리