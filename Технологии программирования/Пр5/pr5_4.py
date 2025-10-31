from collections.abc import Hashable

data = [1, 2, [3, 4], "hello", (5, 6), {"a": 7}, 8, 9]

result_set = set()
for item in data:
    if isinstance(item, Hashable):
        result_set.add(item)

print("Получившееся множество:", result_set)