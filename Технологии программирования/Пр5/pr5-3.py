print("Введи строку или числа через пробел")
vvod = input()
sp = vvod.split()

mn = set(sp)
print("Множество:", mn)
print("Мощность множества:", len(mn))