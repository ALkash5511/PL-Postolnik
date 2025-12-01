# Задание 1.
def ceasar(text, shift):
    try:
        text = str(text)
        shift = int(shift)
        
        letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        
        encoded = ""
        for char in text:
            if char.lower() in letters:
                index = letters.index(char.lower())
                new_index = (index + shift) % len(letters)
                if char.isupper():
                    encoded += letters[new_index].upper()
                else:
                    encoded += letters[new_index]
            else:
                encoded += char
        
        decoded = ""
        for char in encoded:
            if char.lower() in letters:
                index = letters.index(char.lower())
                new_index = (index - shift) % len(letters)
                if char.isupper():
                    decoded += letters[new_index].upper()
                else:
                    decoded += letters[new_index]
            else:
                decoded += char
        
        print("Зашифрованная строка:", encoded)
        print("Расшифрованная строка:", decoded)
    except ValueError as e:
        print("Ошибка ввода чисел:", e)
    except Exception as e:
        print("Неизвестная ошибка:", e)

# text_input = input("Введите предложение: ")
# shift_input = input("Введите сдвиг: ")
# ceasar(text_input, shift_input)


# Задание 2.
def power(x, y=2):
    try:
        if y == 0:
            return 1
        else:
            return x * power(x, y - 1)
    except RecursionError:
        print("Слишком большая степень, рекурсия!")
        return None
    except TypeError:
        print("Неправильный тип данных")
        return None

# try:
#     x = int(input("x="))
#     y = int(input("y="))
#     print(power(x, y))
# except ValueError:
#     print("Нужно вводить целые числа!")
# except Exception as e:
#     print("Ошибка:", e)


# Задание 3.
def find_middle_name():
    try:
        n = int(input("Введите кол-во человек: "))
        middle_names = {}
        count = 0
        
        for i in range(n):
            fio = input("Введите ФИО через пробел: ").split()
            if len(fio) >= 3:
                middle_name = fio[2]
                middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
                count += 1
        
        if middle_names:
            result = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
            print("Самое частое отчество:", result)
        else:
            print("Нет отчеств для подсчета")
        
        print("В расчете участвовало человек:", count)
    except ValueError:
        print("Нужно вводить число!")
    except IndexError:
        print("Не хватает данных в ФИО")
    except Exception as e:
        print("Ошибка:", e)

# find_middle_name()


# Задание 4.
def check_exams():
    необходимые_экзамены = {
        "Информатика": 80,
        "Математика": 85,
        "Русский язык": 75
    }

    print("""Для определения возможности поступления, необходима информация о Вас.

Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
""")

    сданные_экзамены = {}
    try:
        while True:
            ввод = input("").strip()
            if ввод == "":
                break
            
            if "|" not in ввод:
                print("Неправильный формат, используйте |")
                continue
                
            части = [x.strip() for x in ввод.split("|")]
            if len(части) < 2:
                print("Мало данных")
                continue
                
            экзамен = части[0]
            балл_str = части[1]
            сданные_экзамены[экзамен] = int(балл_str)
    except ValueError:
        print("Балл должен быть числом!")
        return
    except Exception as e:
        print("Ошибка:", e)
        return

    print("Ваши экзамены:")
    for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
        print("{} {} {}".format(i, экзамен, балл))

    ok = True
    try:
        for необходимый_экзамен, баллы in необходимые_экзамены.items():
            if необходимый_экзамен not in сданные_экзамены:
                ok = False
                break
            if сданные_экзамены[необходимый_экзамен] < баллы:
                ok = False
                break
    except KeyError:
        ok = False

    if ok:
        print("Вы можете к нам поступить!")
    else:
        print("Увы...")

# check_exams()