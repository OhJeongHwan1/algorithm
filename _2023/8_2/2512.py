N = int(input())
visit = list(map(int, input().split()))
score = int(input())

if sum(visit) <= score :
  print(max(visit))
  exit()

answer = 0
start, end = 0, score
while start <= end :
  mid = (start + end) // 2
  tmp = 0
  for need in visit :
    if need < mid:
      tmp += need
    else:
      tmp += mid
      
  if tmp <= score :
    answer = max(answer, mid)
    start = mid+1
  else :
    end = mid-1

print(answer)