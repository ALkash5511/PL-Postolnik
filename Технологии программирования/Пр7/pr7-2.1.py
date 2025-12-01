print("Вводи числа, 0 - конец")
summ = 0
kolvo = 0
while True:
    ch = int(input())
    if ch == 0:
        break
    summ += ch
    kolvo += 1
print("Сумма:", summ)
print("Количество:", kolvo)