def ceasar(text, shift):
    try:
        text = str(text)
        shift = int(shift)
        
        encoded = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encoded += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
                else:
                    encoded += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            else:
                encoded += char
        
        decoded = ""
        for char in encoded:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
                else:
                    decoded += chr((ord(char) - ord('а') - shift) % 32 + ord('а'))
            else:
                decoded += char
        
        print("Зашифрованная строка:", encoded)
        print("Расшифрованная строка:", decoded)
        
    except ValueError as e:
        print("Ошибка ввода:", e)
    except Exception as e:
        print("Произошла ошибка:", e)

try:
    text = input("Введите предложение: ")
    shift = input("Введите сдвиг: ")
    ceasar(text, shift)
except Exception as e:
    print("Ошибка:", e)