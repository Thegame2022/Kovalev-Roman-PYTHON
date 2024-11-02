# Дано двузначное число. Вывести число, полученное при
# перестановке цифр исходного числа.
# Ввод
while True:
    try:
        number = int(input("Введите двузначное число: "))

        # Проверка, является ли число двузначным
        if 10 <= number <= 99:
            # Меняем местами десятки и единицы
            swapped_number = (number % 10) * 10 + (number // 10)
            print(f"Число после перестановки: {swapped_number}")
            break  # Выходим из цикла, если все хорошо
        else:
            print("Пожалуйста, введите двузначное число!")  # Если не двузначное число
    except ValueError:
        print("Введите корректное число!")  # Обработка некорректного ввода