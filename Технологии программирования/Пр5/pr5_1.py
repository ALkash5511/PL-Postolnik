t = (5, 2, 8, 1, 9)

all_int = True
for item in t:
    if not isinstance(item, int):
        all_int = False
        break

if all_int:
    result = tuple(sorted(t))
else:
    result = t

print(result)