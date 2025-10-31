import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

factorial_8 = math.factorial(8)
numerator = ((x**5 + 9) / factorial_8) * y
denominator = 7 - z % y
a = math.pow(numerator, 1/3) / denominator

print(round(a, 3))