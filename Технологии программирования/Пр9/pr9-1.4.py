try:
    with open("stih.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    print("Стихотворение:")
    print(text)
    
    slova = text.split()
    glas = 0
    soglas = 0
    
    glasnye = "аеёиоуыэюя"
    
    for slovo in slova:
        if slovo and slovo[0].isalpha():
            if slovo[0].lower() in glasnye:
                glas += 1
            else:
                soglas += 1
    
    print("Слов на гласную:", glas)
    print("Слов на согласную:", soglas)
    
    if glas > soglas:
        print("Больше слов на гласную")
    elif soglas > glas:
        print("Больше слов на согласную")
    else:
        print("Поровну")
except FileNotFoundError:
    print("Файл со стихом не найден")
except Exception as e:
    print("Ошибка:", e)