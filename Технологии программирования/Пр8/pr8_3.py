try:
    n = int(input("Введите кол-во человек: "))
    middle_names = {}
    
    for i in range(n):
        fio = input("Введите ФИО через пробел: ").split()
        if len(fio) < 3:
            print("Нет отчества, пропускаем")
            continue
        middle_name = fio[2]
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
    
    if middle_names:
        most_common = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
        print("Самое частое отчество:", most_common)
        print("В расчете участвовало человек:", sum(middle_names.values()))
    else:
        print("Нет людей с отчествами")
        
except ValueError:
    print("Нужно ввести число")
except IndexError:
    print("Неверный формат ФИО")
except Exception as e:
    print("Ошибка:", e)