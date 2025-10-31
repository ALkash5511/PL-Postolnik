text = input("Введите текст: ")

text_no_spaces = text.replace(" ", "")
char_count = {}

for char in text_no_spaces:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

result = ""
for i in range(min(3, len(sorted_chars))):
    if i > 0:
        result += ", "
    result += f"{sorted_chars[i][0]} – {sorted_chars[i][1]} раз"

print(result)