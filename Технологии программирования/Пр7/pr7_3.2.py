p = int(input("Грузоподъемность грузовика (кг): "))
n = int(input("Количество предметов: "))

total = 0
for i in range(n):
    m = float(input(f"Масса предмета {i+1}: "))
    total += m

if total <= p:
    print("Перевозка возможна")
else:
    print("Перевозка невозможна")