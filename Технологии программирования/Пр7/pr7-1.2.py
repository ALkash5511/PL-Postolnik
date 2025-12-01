a = int(input("Первое число: "))
b = int(input("Второе число: "))
if a > b:
    maxi = a
    mini = b
else:
    maxi = b
    mini = a
print("Максимум:", maxi)
print("Минимум:", mini)