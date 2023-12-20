import sys
input = sys.stdin.readline

T = int(input())
x_number = 0
x_num_list =[]
for i in range(T):
    B = int(input())
    number_list = list(map(int, input().split()))

    for number in number_list:
        number = number % 100
        check = int(number/10)


        if check == 1 or check == 6:
            x_number = x_number + 1
        elif check == 2 or check == 7:
            x_number = x_number + 2
        elif check == 3 or check == 8:
            x_number = x_number + 3


    x_num_list.append(x_number)
    x_number = 0


for num in x_num_list:
    print(num)

