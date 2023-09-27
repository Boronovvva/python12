# Циклы for, while 
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

# for number in range(1001): # функция range перешитывает по индексу 
#     print(number)
    
# for py in range(1, 101): # Обязательно в цикле начинается  For а в середине обязательно in 
#     print("Python", py)

# numbers = [10, 3, 4, 1, 3, 45, 101, 123, 112, 9, 90, 99, 101]
# print(type(numbers))
# for num in numbers: 
#     # print(type(num))
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

# mentors = ("Syimyk", 'Islam', 'Kudbuhon', 'Janysh', 'Nur')
# print(mentors)# Итерация по циклу For 
# for mentor in mentors:
#     print("Здраствуйте", mentor)
# # print("Здраствуйте", mentor [0])

# name = "Nurbolot"
# print(name)
# for n in name:
#     print(n)

# nums = []# пустой список можно наполнить функцией range 
# print(nums)
# for num in range(100, 151, 2):
#     nums.append(num)
# print(nums)

# while True:
#     print("Geeks")
# num1 = 10
# num2 = 30
# while num2 > num1:
#     num1 += 1 
#     print(num1)
# n = 0 
# while True:
#     n += 1 
#     print("Geeks", n)
#     if n == 20000:
#         print("Stop")
#         break # заставляет прервать цикл досрочно и всегда пищется в конце условия 
#     elif n == 19998:
#         print("CONTINUE")
#         continue # продолжает цикл без остановки 

# import random
# letters = 'qwertyuiopasdfghjklzxcvbnm123456789'

# result = ""
# len_password = int(input('Длина пароля: '))
# for i in range(len_password):
#     random_letter = random.choice(letters) # choise выбирает рандомно
#     result += random_letter
# print(result)

# import random
# cities = ["Osh", "Bishkek", "Batken", "Naryn", "Talas"]
# random_city = random.choice(cities)
# n = 0
# while True:
#     if n == 3:
#         print("У вас закончились попытки")
#         break 
#     user_city = input("Город: ")
#     if random_city == user_city:
#         print("Вы выиграли!")
#         break 
#     else:
#         n += 1
#         print("Неправильно, у вас", 3 - n, "попыток")
