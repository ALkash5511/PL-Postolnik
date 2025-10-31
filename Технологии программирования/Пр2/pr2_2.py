x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

fac8 = 1*2*3*4*5*6*7*8
numerator = ((x**5 + 9) / fac8) * y
denominator = 7 - z % y
a = numerator**(1/3) / denominator

print(round(a, 3))