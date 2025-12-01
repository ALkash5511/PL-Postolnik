try:
    with open("chisla.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    chisla = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                chisla.append(float(line))
            except:
                continue
    
    if chisla:
        summ = sum(chisla)
        maxi = max(chisla)
    else:
        summ = 0
        maxi = 0
    
    with open("chisla.txt", "a", encoding="utf-8") as f:
        f.write("\n" + str(summ) + "\n" + str(maxi))
    
    print("Сумма:", summ)
    print("Максимум:", maxi)
    print("Добавлено в файл")
except FileNotFoundError:
    print("Файл не найден!")
except Exception as e:
    print("Ошибка:", e)