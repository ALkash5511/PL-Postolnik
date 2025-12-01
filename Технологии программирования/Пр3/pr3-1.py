print("Введи название футбольной команды")
komanda = input()

print(komanda, "- чемпион!")

dlina = len(komanda)
cherta = "-" * dlina
print(cherta)

komanda_mal = komanda.lower()
print("Длина названия:", len(komanda_mal))

est_p = "п" in komanda_mal
print("Есть буква 'п'?", est_p)

skoka_a = komanda_mal.count("а")
print("Буква 'а' встречается раз:", skoka_a)