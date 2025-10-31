try:
    with open("poem.txt", "r", encoding="utf-8") as f:
        poem = f.read()
    
    print("Стихотворение:")
    print(poem)
    
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    
    vowel_count = 0
    consonant_count = 0
    
    words = poem.split()
    for word in words:
        if word and word[0].isalpha():
            first_char = word[0].lower()
            if first_char in vowels:
                vowel_count += 1
            elif first_char in consonants:
                consonant_count += 1
    
    print(f"\nСлов на гласную: {vowel_count}")
    print(f"Слов на согласную: {consonant_count}")
    
    if vowel_count > consonant_count:
        print("Больше слов на гласную букву")
    elif consonant_count > vowel_count:
        print("Больше слов на согласную букву")
    else:
        print("Одинаковое количество")
        
except FileNotFoundError:
    print("Файл poem.txt не найден")
except Exception as e:
    print("Ошибка:", e)