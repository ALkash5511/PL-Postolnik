a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    max_num = a
    min_num = b
else:
    max_num = b
    min_num = a

print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")