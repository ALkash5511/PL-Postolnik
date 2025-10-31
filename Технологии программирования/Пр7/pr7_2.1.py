print("Введите последовательность чисел (0 для окончания):")
total = 0
count = 0

num = int(input())
while num != 0:
    total += num
    count += 1
    num = int(input())

print(f"Сумма: {total}")
print(f"Количество: {count}")