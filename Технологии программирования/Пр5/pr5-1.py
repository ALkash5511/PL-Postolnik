print("Введи кортеж чисел через пробел")
vvod = input()
spisok = vvod.split()
kor = tuple(spisok)

vse_cel = True
for elem in kor:
    if not elem.isdigit():
        vse_cel = False
        break

if vse_cel:
    kor_chisla = tuple(map(int, kor))
    kor_sort = tuple(sorted(kor_chisla))
    print("Отсортированный кортеж:", kor_sort)
else:
    print("Исходный кортеж:", kor)