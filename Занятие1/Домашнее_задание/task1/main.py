speed = int(input('введите скорость передачи данных, байт: '))
time = int(input('введите время скачивания, секунд: '))
acoast_ = int(input('стоимость одного Гбайт, руб: '))
Gb_speed = speed / 1073741824
file_size_Gb = Gb_speed * time
money_pay = (file_size_Gb - 1) * acoast_
print(file_size_Gb)
print(money_pay)

