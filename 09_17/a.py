N,M,K=map(int, input().split())
num_list = []
for i in range(M):
    num_list.append(list(map(int, input().split())))

num_list.sort(reverse=True)

problem_number = K
index = 0
result = 0
for i in range(K,0,-1):
    if problem_number == 0:
        break
    if num_list[index][1] == 0:
        index+=1
    minus = min(problem_number,num_list[index][1])
    result += num_list[index][0] * minus
    num_list[index][1] = 0
    problem_number = problem_number - minus
    
print(result)
    