a = int(input("От: "))
b = int(input("До: "))
c = int(input("Кратно: "))
for i in range(a, b+1):
    if i % c == 0:
        print(i, end=" ")
print()