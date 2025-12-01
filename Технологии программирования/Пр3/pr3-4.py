print("Введи строку:")
st = input()
print("Введи подстроку для поиска:")
subst = input()

st_mal = st.lower()
subst_mal = subst.lower()

if subst_mal in st_mal:
    print("Подстрока есть")
else:
    print("Подстроки нет")