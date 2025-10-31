a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
m = float(input("Введите m: "))
n = float(input("Введите n: "))

d = b**2 - 4*a*c

if d < 0:
    print("Решений нет")
elif d == 0:
    x = -b / (2*a)
    if m <= x <= n:
        print(f"Решение {x} попадает в отрезок")
    else:
        print(f"Решение {x} не попадает в отрезок")
else:
    x1 = (-b - d**0.5) / (2*a)
    x2 = (-b + d**0.5) / (2*a)
    
    in_range1 = m <= x1 <= n
    in_range2 = m <= x2 <= n
    
    if in_range1 or in_range2:
        print("Хотя бы одно решение попадает в отрезок")
    else:
        print("Оба решения не попадают в отрезок")