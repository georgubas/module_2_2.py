print('Введите три числа')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('3')
elif second == third or second == first or third == first:
    print('2')
else:
    print('0')