print("Вводи числа, 0 - стоп")
summ = 0
kol = 0
while True:
    ch = int(input())
    if ch == 0:
        break
    summ += ch
    kol += 1
print("Сумма:", summ)
print("Кол-во:", kol)