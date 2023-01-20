# 4. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

amount_friends = int(input('Введите количество друзей: '))
dict_friends = {}

for i in range(amount_friends):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    dict_friends[name] = age

friends = list(dict_friends.items())
print('Список друзей:', friends)

count = 0
for name, age in dict_friends.items():
    count += age
count /= amount_friends
print('Средний возраст всех друзей:', count)

max_name = max(dict_friends, key = len)
for name, age in dict_friends.items():
        if len(name) == len(max_name):
            print('Самое длинное имя:', name)

