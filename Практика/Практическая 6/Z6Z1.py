n = input("Введите любую строку: ")
s = n.split( )
i = 0
count = 0
for i in s:
    p = i.find("е")
    if p==0:
        count+=1
print(count)