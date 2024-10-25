a = int(input("Введите целое число A "))
b = int(input("Введите целое число B "))
if a>b:
    for i in range(a, b-1, -1):
        if i<0:
            print(i, end=" ")
else:
    print("Число A меньше B!")