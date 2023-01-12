import random

#Завдання  3
print('Завдання 3 \'Список парні, непарні\'')
my_list_1 = random.sample(range(1, 200), 10)
my_list_2 = random.sample(range(1, 200), 10)
my_result = []
print(f'my_list = {my_list_1}')
print(f'my_list = {my_list_2}')

for i in range(len(my_list_1)):
    if i % 2 == 0:
        my_result.append(my_list_1[i])
    else:
        my_result.append(my_list_2[i])
print(f'my_result = {my_result}')


#Завдання  11

print('Завдання  11 \'Унікальні символи зі строки\'')
my_str = '123232321567880'
my_result = []
exec("""\nfor i in list(my_str):\n\t if list(my_str).count(i) == 1:\n\t\t  my_result.append(i)\n""")
print(f'my_str = {my_str}')
print(f'my_result = {my_result}')