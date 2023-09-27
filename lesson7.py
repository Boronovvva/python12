# Dictionary - словари 
# Типы данных: list, tuple, int, str, float, bool, set, frozenset, dict
# student = {'name':'Nurbolot', 'age':19}# dict изменяемый 
# print(type(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python')# setdefault метод для добавления в список 
# print(student)
# student.pop('age')# pop метод удаления из списка по ключу
# print(student)
# student['language'] = "Java"# синтаксис для обновления значения по ключу
# print(student)
# print(student.keys())# метод для получения ключей из словаря 
# print(student.values())# метод для получения значений из словаря
# print(student.items())# метод для получения ключа и значения за раз из словаря

# geeks = {'name':'Geeks', 'count_students':340, 'address':'Amatova 1B'}
# print(geeks)
# for key, value in geeks.items():
#     print(key, value)

# dct = {}
# print(type(dct))

# contact = {'MCHS':112}
# while True:
#     command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Имя: ")
#         add_number = input("Номер: ")
#         contact.setdefault(add_name, add_number)
#         print("Контакт", add_name, "успешно добавлен")
#     elif command == "3":
#         remove_name = input("Кого удалить? ")
#         contact.pop(remove_name)
#         print("Контакт", remove_name, "успешно удален")
#     elif command == "4":
#         update_name = input("Кого обновить? ")
#         update_number = input("Новый номер: ")
#         contact[update_number] = update_number
#         print("Номер контакта", update_name, "Успешно обнавлен на", update_number)
#     else:
#         print("Такой команды нету")

# Functions - функции 
# def hello():
#     print("Hello world")
# hello()

# def welcome():
#     name = input("Имя: ")
#     print("Привет", name)
# welcome()

# def add():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 + num2)
# add()

# def mult(num1, num2): # num1 u num2 являются параметром функции mult
#     print(num1 + num2)
# mult(5, 3)# Числа 5 3 являются аргументами функции 
# mult(15, 30)

# def div(num_1, num_2):
#     try:
#         print(num_1 / num_2)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
# div(10, 5)
# div(10, 0)