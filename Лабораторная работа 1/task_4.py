users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

print({
    "Общее количество": len(users),
    "Уникальные посещения": len(set(users))
})