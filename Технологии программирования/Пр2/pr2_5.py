m = int(input("Введите количество минут: "))

hours = m // 60
minutes = m % 60

print(f"Целых часов: {hours}")
print(f"Минут с начала последнего часа: {minutes}")