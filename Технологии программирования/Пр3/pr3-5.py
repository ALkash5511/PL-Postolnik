print("Введи строку:")
stroka = input()
print("Какую букву ищем?")
bukva = input()

if bukva in stroka:
    perv_index = stroka.index(bukva)
    posl_index = stroka.rindex(bukva)
    print("Первое вхождение на позиции:", perv_index)
    print("Последнее вхождение на позиции:", posl_index)
else:
    print("Такой буквы в строке нет")