print("Введи a, b, c для уравнения")
a = float(input())
b = float(input())
c = float(input())

print("Теперь отрезок m и n")
m = float(input())
n = float(input())

D = b*b - 4*a*c

if D < 0:
    print("Корней нет вообще")
elif D == 0:
    x = -b / (2*a)
    print("Корень один:", x)
    if m <= x <= n:
        print("Да, в отрезок попал")
    else:
        print("Нет, не попал")
else:
    import math
    kd = math.sqrt(D)
    x1 = (-b + kd) / (2*a)
    x2 = (-b - kd) / (2*a)
    print("Два корня:", x1, "и", x2)
    pop1 = m <= x1 <= n
    pop2 = m <= x2 <= n
    if pop1 or pop2:
        print("Хотя бы один корень в отрезке")
    else:
        print("Ни один корень не в отрезке")