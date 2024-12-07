def fun(p=0):    
    n = int(input("Введите число: "))
    if n == 0:        
        return p
    else:        
        p = max(p, n)
        return fun(p)
print("Максимальное число из получившейся последовательности: ", fun(0))