# Исключения 
# try, except

# try:
#     num1 = 10
#     num2 = 0 
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         print(f"Результат после сложения: {num1+num2}")
#         print(f"Результат после вычитания: {num1-num2}")
#     except ValueError:
#         print(f"Введите числа!!!")

# тип данные set, frozenset 
# тип данных set не имеет дубликатов, и не имеет структуры и порядка
# в сет не можем использовать индексы и срезы 
# сет изменяемый тип данных
# num = {2,3,4,5,6,1,3}
# print(num)
# print(type(num))

# name = {"geeks", "Abu", "Kutbu", "Nurbu", "geeks"}
# print(name)

# num = {1,2,3,4,5,"1"}
# print(num)

# try:
#     num = {1,2,3,4,5,6,7,8}
#     print(num[3])
# except:
#     print("set() не можем использовать индексы и срезы ")

# num = {1,2,3,4}
# num.add(5)
# num.add(5)
# print(num)
# num.remove(2)
# print(num)

# name = frozenset(["Nurti", "Kumi", "Toxa", "Kumi"])
# print(type(name))
# print(name)
# name.add("AbuDabu")
# print(name)
# name.remove("Kumi")
# print(name)
# frozenset не изменяемый 