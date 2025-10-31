# 1. Создание словаря
info = {}

info["фио"] = "Постольник Альберт Кимович"
info["дата рождения"] = "17/02/2007"
info["место рождения"] = "ДНР"

print(info)

info["хобби"] = ["спорт", "лежать на диване"]
info["хобби"].append("программирование")

info["животные"] = ("Лютик")

info["ЕГЭ"] = {}

info["ЕГЭ"]["Математика"] = 72
info["ЕГЭ"]["Информатика"] = 55
info["ЕГЭ"]["Русский язык"] = 67

info["ЕГЭ"]["Физика"] = 0
del info["ЕГЭ"]["Физика"]

info["вузы"] = {}

info["вузы"]["ВГУИТ"] = 180
info["вузы"]["ВГТУ"] = 190
info["вузы"]["ВГЛТУ"] = 200

# 2. Вывод на экран
print("Данные:")
print(info)

exams = sorted(info["ЕГЭ"].keys())
print("Предметы:", ", ".join(exams))

uni = sorted(info["вузы"].keys())
print("Вузы:", ", ".join(uni))

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

name = info["фио"].split()[1]
starts_with_vowel = name[0].lower() in 'аеёиоуыэюя'
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info["дата рождения"].split('/')[1])
born_in_winter_or_summer = month in [12, 1, 2, 6, 7, 8]
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

exams_count = len(info["ЕГЭ"])
print("* после окончания школы сдавал {} экз.".format(exams_count))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = sum(1 for score in info["вузы"].values() if sum_mark >= score)
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))