# Дз 1 
#for i in range(1, 6):
#     print(f"{i}. 0")

# # Дз 2 
# numbers = []

# for i in range(1, 101):
#     numbers.append(i)

# print(numbers)

# Дз 3 
# for num in range(1, 497): 
#     if num % 2 == 0:
#         print(num, "четный")

# Дз 4 
# numbers = list(range(1, 1001))
# print("Минимальное число:", min(numbers))
# print("Максимальное число:", max(numbers))
# print("Сумма чисел:", sum(numbers))

# Дз 5 
# lst = [0 for i in range(100)]
# print(lst)

# Дз 6
# it_company = ('Google', 'Amazon', 'Microsoft')
# it_company_list = list(it_company)
# it_company_list.append('Tesla')

# print(it_company_list)
# it_company_tuple = tuple(it_company_list)
# print(it_company_tuple)

# index_amazon = it_company_tuple.index('Amazon')
# print(index_amazon)

# it_company_list[it_company_list.index('Google')] = 'Apple'
# print(it_company_list)


# sliced_list = it_company_list[it_company_list.index('Apple'):it_company_list.index('Microsoft')]
# print(sliced_list)
      
#Дз 10
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other',
# 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the',
# 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your',
# 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count('Python'))

# Дз 11
# a = input("Введите значение переменной a: ")
# b = input("Введите значение переменной b: ")

# a, b = b, a

# print("Новые значения:")
# print("a =", a)
# print("b =", b)

# Дз 12 
# while True:
#     age = int(input("Введите ваш возраст: "))

#     if age >= 18:
#         print("Доступ разрешен")
#         break
#     else:
#         print("Извините, пользование данным ресурсом только с 18 лет")
#         continue


