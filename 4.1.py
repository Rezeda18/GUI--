def z1():
    if int(input()) % 3 == 0:
        print("Ваше число делится на 3")
    else:
        print("Ваше число не делится на 3")

def z2():
    try:
        a = int(input('Введите число, на которое будем делить: '))
        b = 100 / a
    except ZeroDivisionError:
        print('Ваше число равно 0!')
    except ValueError:
        print('Введено не число!')
    print(b)

def z3():
    a = input('Введите дату: ')
    b = a.split('.')
    c = int(b[2]) % 100
    d = int(b[0]) * int(b[1])

    if d == c:
        print('Ваша дата является магической <3')
    else:
        print('Ваша дата не магическая')

def z4():
    a = input('Введите номер билета: ')
    a1 = int(len(a))
    b = int(a1 / 2)
    sum1 = 0
    sum2 = 0

    if a1 % 2 == 0:
        for i in range(b):
            sum1 += int(a[i])
        for j in range(b, a1):
            sum2 += int(a[j])
        if sum1 == sum2:
            print('Ваш билет счастливый!')
        else:
            print('Ваш билет обычный)')
    else:
        print('Длина вашего билета нечётная!')

    print(sum1, sum2)