numbers = input("Введите числа через пробел: ").split()

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(num + "\n")

print("Числа записаны в файл numbers.txt")