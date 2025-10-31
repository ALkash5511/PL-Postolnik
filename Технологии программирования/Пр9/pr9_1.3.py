try:
    with open("numbers.txt", "r") as f:
        content = f.read()
    
    lines = content.split('\n')
    numbers = []
    
    for line in lines:
        try:
            num = float(line.strip())
            numbers.append(num)
        except:
            continue
    
    if numbers:
        total = sum(numbers)
        maximum = max(numbers)
        
        with open("numbers.txt", "a") as f:
            f.write(f"\n{total} {maximum}")
        
        print(f"Сумма: {total}, Максимум: {maximum}")
    else:
        print("Чисел не найдено")
        
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Ошибка:", e)