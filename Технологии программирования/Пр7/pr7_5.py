a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a < b:
    start = a
    end = b
else:
    start = b
    end = a

print(f"Числа кратные {c}:")
for i in range(start, end + 1):
    if i % c == 0:
        print(i, end=" ")