
number = [i+1 for i in range(10000)]

for i in range(10000):
    if number[i] !=0:
        num = number[i]
        while num <= 10000:
            thousand = int(num/1000)
            hundred = int((num-thousand*1000)/100)
            ten =  int((num-thousand*1000-hundred*100)/10)
            one =  int((num-thousand*1000-hundred*100-ten*10))
            num = num + thousand + hundred + ten + one
            if num > 10000:
                break
            number[num-1] = 0

for num in number:
    if num !=0:
        print(num)

        