def task2():
    # Одномерный массив из 10-и целых чисел
    numbers = []

    # Заполнить массив с клавиатуры
    for i in range(10):
        num = int(input(f"Введите число {i+1}: "))
        numbers.append(num)

    # Определить сумму тех чисел, которые строго больше 5
    sum_greater_than_5 = sum(num for num in numbers if num > 5)
    print("Сумма чисел, строго больше 5:", sum_greater_than_5)

# Вызов функции
task2()
