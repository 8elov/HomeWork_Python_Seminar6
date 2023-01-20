# 3. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

amount_friends = int(input('Введите количество друзей: '))
dict_friends = {}

for i in range(amount_friends):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    dict_friends[name] = age
# friends.append(dict_friends)

friends = list(dict_friends.items())
print('Список друзей:', friends)

max_value = min(dict_friends.values())
for name, age in dict_friends.items():
        if age == max_value:
            print('Самый младший друг:', name)

