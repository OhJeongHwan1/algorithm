try:
    x = int(input('나눌 숫자를 입력하시오!: '))
    y = 10/x
    print(y)
except ZeroDivisionError as error:
    print('0으로 나눌 수 있겠냐.',error)

except ValueError as error:
    print('정수만 입력가능',error)
finally:
    print('나라는 것은')