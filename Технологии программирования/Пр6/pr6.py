# 1. Создание словаря
info = {}

info["фис"] = "Петров Алексей Сергеевич"
info["дата рождения"] = "15/07/2000"
info["место рождения"] = "Москва"

print(info)

info["хобби"] = ["футбол", "чтение"]
info["хобби"].append("программирование")

info["животные"] = ("собака Шарик", "кот Васька")

info["ЕГЭ"] = {}

info["ЕГЭ"]["Математика"] = 85
info["ЕГЭ"]["Информатика"] = 90
info["ЕГЭ"]["Русский язык"] = 78

info["ЕГЭ"]["Физика"] = 0
del info["ЕГЭ"]["Физика"]

info["вузы"] = {}

info["вузы"]["МИРЭА"] = 240
info["вузы"]["МГУ"] = 295
info["вузы"]["МГТУ им. Баумана"] = 260

# 2. Вывод на экран
print("\nДанные:")
print(info)

exams = sorted(info["ЕГЭ"].keys())
print("Предметы:", exams)

uni = sorted(info["вузы"].keys())
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

name = info["фис"].split()[1]
starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info["дата рождения"].split("/")[1])
born_in_winter_or_summer = month in [12,1,2,6,7,8]
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
first_hobby = info["хобби"][0]
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, first_hobby))

exam_count = len(info["ЕГЭ"])
print("* после окончания школы сдавал {} экз.".format(exam_count))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = 0
sum_ball = sum_mark
for ball in info["вузы"].values():
    if sum_ball >= ball:
        vuz_count += 1
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))