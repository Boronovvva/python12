# Условия if, tlse, elif 

# print(10==5)
# print(500==500)

# print(20!=10)
# print(2!=2)

# print(10>5)
# print(30>400)

# print(30<500)
# print(5<5)

# print(30>=30)
# print(40>=400)

# print(50<=50)
# print(500<=10)

# num1 = 10 
# num2 = 20
# if num1 > num2: # Условие работает когда значение True 
#     print("num1 больше") # Пробел обезятельно 
# else: 
#     print('num2 больше')

# number = int(input("Число:"))
# if number % 2 ==0 : # % деление по модулю когда делимое без остатка 
#     print(number, "четный")
# else:
#     print(number, "нечетный")    

# school_class = int(input("Kласс:"))
# if school_class < 5:
#     print("Начальный класс")
# elif school_class < 9:
#     print("Средний класс")
# elif school_class<12:
#     print("Старший каласс")
# else:
#     print("Такого класса нету")

# login =input("login: ")
# password = input("password: ")
# if login =="geeks":
#     if password == "geeksstudents":
#         print("Welcome", login)
#     else:
#         print("password error")
# else:
#     print("login error")

# login =input("login: ")
# password = input("password: ")
# if login == "geeks" and password == "geeeksstudents":
#     print("Welcome", login)
# else:
#     print("Error login or passsword")

# number1= int(input("Первое число:"))
# operator = input("+,-,*,/: ")
# number2 = int(input("Второе число") )
# if operator == "+":
#     print(number1 + number2)
# elif operator == "-":
#     print(number1-number2)
# elif operator == "*":
#     print(number1*number2)
# elif operator == "/":
#     print(number1/number2)
# else: 
#     print("Такого оператора нету")

# import random

# random_number = random.randint(1,5)
# # print(random_number)
# user_number = int(input("Число:"))
# if user_number >= 1 and user_number <=5:
#     if user_number == random_number:
#         print("Вы угадали!")
#     else:
#         print("Вы не откадали число",random_number)
# else:
#     print("Введите число только от 1 до 5")