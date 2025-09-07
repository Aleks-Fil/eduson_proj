# Получение коэффицентов
first_coefficint = int(input('a = ',))
second_coefficint = int(input('b = ',))
third_coefficint = int(input('c = ',))

# Решение по сокращенной формуле, т.к. b - четное
if first_coefficint != 0 and second_coefficint % 2 == 0 and third_coefficint != 0:
    k = second_coefficint / 2
    d1 = k ** 2 - first_coefficint * third_coefficint
    root_1 = (-k + d1 ** 0.5) / first_coefficint
    root_2 = (-k - d1 ** 0.5) / first_coefficint

    print('Так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'первый корень: {root_1}')
    print(f'второй корень: {root_2}')

# Решение уравнения при с = 0
if first_coefficint != 0 and third_coefficint == 0 and second_coefficint != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_coefficint / first_coefficint}')

# Решение уравнения при b = 0 и c = 0
if first_coefficint != 0 and second_coefficint == 0 and third_coefficint == 0:
    print(f'корни уравнения равны нулю, first_coefficint * x ** 2 = 0')

# Решение полного уравнения
if first_coefficint != 0 and second_coefficint % 2 != 0 and third_coefficint != 0:
    d = second_coefficint ** 2 - 4 * first_coefficint * third_coefficint
    if d > 0:
        # решение уравнения при b = 0 и c = 0
        if first_coefficint != 0 and second_coefficint == 0 and third_coefficint == 0:
        root_1 = (-second_coefficint + d ** 0.5) / (2 * first_coefficint)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(root_1, 2)}')
        root_2 = (-second_coefficint - d ** 0.5) / (2 * first_coefficint)
        print(f'второй корень равен: {round(root_2, 2)}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет') 
    else:
        k = -second_coefficint / (2 * first_coefficint)
        print(f'уравнение имеет один корень: {k}')

        # решение уравнения при b = 0
        if first_coefficint != 0 and third_coefficint != 0 and second_coefficint == 0:
            if (- third_coefficint / first_coefficint) >= 0:
                root_1 = (-third_coefficint / first_coefficint) ** 0.5
                print(f'первый корень равен: {root_1}')
                root_2 = (-1) * (( -third_coefficint / first_coefficint) ** 0.5)
                print(f'второй корень равен: {root_2}')
        if ( - third_coefficint / first_coefficint) < 0:
            print(
            f' third_coefficint / first_coefficint = : {-third_coefficint / first_coefficint},'
                  f'т.е. < 0, поэтому действительных корней нет')

