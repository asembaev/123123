while True:
    number = int(input("Введите число: "))
    if number < 0:
        print("Число меньше 0. Пропускаем этот шаг.")
        continue
    else:
        print("Введённое число:", number)
        break
