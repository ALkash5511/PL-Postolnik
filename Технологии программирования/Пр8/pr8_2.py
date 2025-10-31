def power(x, y=2):
    try:
        if y == 0:
            return 1
        else:
            return x * power(x, y - 1)
    except RecursionError:
        print("Слишком большая степень")
        return 0
    except Exception as e:
        print("Ошибка:", e)
        return 0

try:
    x = int(input("x="))
    y = int(input("y="))
    result = power(x, y)
    print(result)
except ValueError:
    print("Нужно вводить целые числа")
except Exception as e:
    print("Ошибка:", e)