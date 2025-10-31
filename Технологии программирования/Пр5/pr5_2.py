t = (1, 2, 3, 4, 2, 5, 6)
element = 2

if element in t:
    first_index = t.index(element)
    try:
        second_index = t.index(element, first_index + 1)
        result = t[first_index:second_index + 1]
    except ValueError:
        result = t[first_index:]
else:
    result = ()

print(result)