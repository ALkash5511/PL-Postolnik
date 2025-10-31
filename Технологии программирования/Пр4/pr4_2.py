strings = ["автобус", "ок", "чокопайка", "пирог", "абобус"]

max_length = 0
for s in strings:
    if len(s) > max_length:
        max_length = len(s)

new_list = []
for s in strings:
    if len(s) < max_length:
        s = s + "_" * (max_length - len(s))
    new_list.append(s)

print("Исходный список:", strings)
print("Новый список:", new_list)