a,b = map(int,input().split())

num = 1
while True:
    if(a==b):
        print(num)
        break
    if(a>b):
        print(-1)
        break
    if(b%2 == 0):
        b = b/2
    elif(b%10 == 1):
        b = (b-1)/10
    elif(a<b and b%10 != 1):
        print(-1)
        break
    num = num + 1
