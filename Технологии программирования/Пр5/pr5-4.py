from collections.abc import Hashable

spisok = [1, "привет", [1,2], 3.14, {"ключ": "знач"}, (5,6), "мир", 100]
mn = set()

for item in spisok:
    if isinstance(item, Hashable):
        mn.add(item)

print("Получившееся множество:", mn)