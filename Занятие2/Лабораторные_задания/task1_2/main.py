a = int(input('Введите число A'))
b = int(input('Введите число B'))

result = a % 2 == 1 and b % 2 == 1
if result:
    print("Числа A и B нечетные")