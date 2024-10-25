a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B: "))
if a <= b:
    for i in range(a,b+1):
        print (i, end=" ")
else:
    print("Число A больше B!")