x = int(input("Введите число Х: "))
n = int(input("Введите число N: "))
def fuc(n):
    if n == 0:
        return 1
    return fuc(n-1) * n
print(f"Результат рекурсивных вычислений: {(x**n)/fuc(n):.2f}")
