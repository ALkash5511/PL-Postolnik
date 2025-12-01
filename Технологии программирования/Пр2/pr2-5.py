print("Введи два числа, целых")
ch1 = int(input("Первое: "))
ch2 = int(input("Второе: "))

print("Плюс:", ch1 + ch2)
print("Минус:", ch1 - ch2)
print("Умножить:", ch1 * ch2)

d = ch1 / ch2
print("Делить:", round(d, 2))

print("Целая часть от деления:", ch1 // ch2)
print("Остаток от деления:", ch1 % ch2)
print("Степень:", ch1 ** ch2)

print("Сравниваем:")
print(ch1, "<", ch2, "=", ch1 < ch2)
print(ch1, "<=", ch2, "=", ch1 <= ch2)
print(ch1, ">", ch2, "=", ch1 > ch2)
print(ch1, ">=", ch2, "=", ch1 >= ch2)
print(ch1, "!=", ch2, "=", ch1 != ch2)
print(ch1, "==", ch2, "=", ch1 == ch2)