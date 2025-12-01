print("Введи кортеж чисел через пробел")
vvod = input()
sp = vvod.split()
kor = tuple(map(int, sp))

print("Введи элемент для поиска")
elem = int(input())

if elem in kor:
    perv_index = kor.index(elem)
    vtor_index = kor.index(elem, perv_index + 1) if kor.count(elem) > 1 else len(kor) - 1
    noviy_kor = kor[perv_index:vtor_index+1]
    print("Новый кортеж:", noviy_kor)
else:
    print("Пустой кортеж:", tuple())