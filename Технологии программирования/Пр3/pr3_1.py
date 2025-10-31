team = input("Введите название футбольной команды: ")
print(team + " - чемпион!")

line = "-" * len(team)
print(line)

team_lower = team.lower()
print("Длина названия:", len(team_lower))
print("Есть ли буква 'п':", "п" in team_lower)
print("Количество букв 'а':", team_lower.count("а"))