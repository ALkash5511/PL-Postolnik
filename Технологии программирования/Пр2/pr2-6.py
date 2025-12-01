print("Давай x, y, z через Enter")
x = int(input())
y = int(input())
z = int(input())

fact = 1
for i in range(1, 9):
    fact = fact * i

verh = (x**5 + 9) / fact * y
kub_koren = verh ** (1/3)
niz = 7 - z % y

if niz == 0:
    print("На ноль делить низя!")
else:
    otvet = kub_koren / niz
    print("Вот что вышло:", round(otvet, 3))