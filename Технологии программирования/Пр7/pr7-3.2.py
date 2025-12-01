p = int(input("Грузоподъемность: "))
n = int(input("Сколько предметов: "))
summ = 0
for i in range(n):
    m = int(input(f"Масса {i+1}: "))
    summ += m
if summ <= p:
    print("Перевозка возможна")
else:
    print("Перевозка невозможна")