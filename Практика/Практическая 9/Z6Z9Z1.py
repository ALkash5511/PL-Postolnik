matrix = [[1, 4, 5],
          [3, 2, 7],
          [8, 6, 9]]

max_in_rows = [max(row) for row in matrix]
min_in_cols = [min(col) for col in zip(*matrix)]

print("Наибольшие элементы в каждой строке:", max_in_rows)
print("Наименьшие элементы в каждом столбце:", min_in_cols)