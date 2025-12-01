vvod = input("Введите числа через пробел: ")
chisla = vvod.split()
with open("chisla.txt", "w", encoding="utf-8") as f:
    for ch in chisla:
        f.write(ch + "\n")
print("Записано в файл chisla.txt")