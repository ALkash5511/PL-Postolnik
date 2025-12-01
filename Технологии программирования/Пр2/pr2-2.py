print("Минуты с начала дня?")
minutki = int(input())

chasiki = minutki // 60
ost_min = minutki % 60

print("Часов прошло:", chasiki)
print("Минут с начала часа:", ost_min)