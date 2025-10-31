print("Введите последовательность (0 для окончания):")
total = 0
count = 0

while True:
    num = int(input())
    if num == 0:
        break
    total += num
    count += 1

print(f"Сумма: {total}")
print(f"Количество: {count}")