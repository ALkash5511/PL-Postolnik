a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a < b:
    start = a
    end = b
else:
    start = b
    end = a

print("Числа от минимального до максимального:")
for i in range(start, end + 1):
    print(i, end=" ")

print("\nЧисла от максимального до минимального:")
for i in range(end, start - 1, -1):
    print(i)