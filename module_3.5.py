def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        first = int(str_number[0])  # Берем первую цифру
        # Умножаем первую цифру на результат рекурсивного вызова с оставшимися цифрами
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру
        return int(str_number)

# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)