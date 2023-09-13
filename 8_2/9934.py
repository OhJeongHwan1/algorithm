n = int(input())
seq = list(map(int,(input().split())))
start = 0
endd = len(seq)-1
level = [[] for _ in range(n)]

def check (seq,start,endd,x):
    mid = (start + endd)//2
    if(mid == start):
        level[x].append(seq[start])
        return
    if(mid == endd):
        level[x].append(seq[endd])
        return
    level[x].append(seq[mid])
    check(seq,start,mid-1,x+1)
    check(seq,mid+1,endd,x+1)

x=0
check(seq,start,endd,x)

for i in range(n):
    print(*level[i])


