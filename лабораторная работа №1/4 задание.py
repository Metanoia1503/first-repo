users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
unique=len(set(users))
total = len(users)

stats = {
    "Общее количество": total,
    "Уникальные посещения": unique}


print(stats)
