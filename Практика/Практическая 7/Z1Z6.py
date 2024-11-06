def task1():
    # Дан одномерный массив из 10 целых чисел
    numbers = [12, 11, 13, 5, 6, 7, 8, 9, 10, 15]

    # Найти среднеарифметическое
    average = sum(numbers) / len(numbers)
    print("Среднеарифметическое:", average)

    # Сравнить среднеарифметическое с остальными элементами
    less_than_max = sum(1 for num in numbers if num < max(numbers))
    greater_than_average = sum(1 for num in numbers if num > average)

    print("Количество чисел, меньше максимального:", less_than_max)
    print("Количество чисел, больше среднеарифметического:", greater_than_average)

# Вызов функции
task1()