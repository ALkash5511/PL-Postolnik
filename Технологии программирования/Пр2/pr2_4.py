num2 = int(input("Введите двузначное число: "))
num3 = int(input("Введите трехзначное число: "))

a2 = num2 // 10
b2 = num2 % 10
sum2 = a2 + b2
prod2 = a2 * b2

a3 = num3 // 100
b3 = (num3 // 10) % 10
c3 = num3 % 10
sum3 = a3 + b3 + c3
prod3 = a3 * b3 * c3

print(f"Двузначное: сумма = {sum2}, произведение = {prod2}")
print(f"Трехзначное: сумма = {sum3}, произведение = {prod3}")