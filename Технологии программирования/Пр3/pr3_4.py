st = input("Введите строку: ")
subst = input("Введите подстроку для поиска: ")

if subst.lower() in st.lower():
    print("Подстрока есть")
else:
    print("Подстроки нет")