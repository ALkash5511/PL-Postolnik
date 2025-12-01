x = float(input("Введите x: "))
if x >= 0:
    f = (x + x**2)**0.5
else:
    f = 1 / x
print("f =", round(f, 2))