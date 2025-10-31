text = input("Введите строку: ")
letter = input("Введите букву для поиска: ")

if letter in text:
    first_index = text.index(letter)
    last_index = text.rindex(letter)
    print("Первый индекс:", first_index)
    print("Последний индекс:", last_index)
else:
    print("Буква не найдена в строке")