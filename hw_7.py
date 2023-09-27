# Дз 1 
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
# dictionary_1

# Дз 2 
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' :3, 'num_100' : 100}
# for key,value in numbers.items():
#     numbers[key] = value * 5
# print(numbers)

# Дз 3 
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *=2
# print(student)

#Дз 4
# student = {'name' : 'Askhat', 'age' : 17 ,'color' : 'White'}
# student['age'] = 16
# print(student)

# Дз 5
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

# Дз 6
# student = {'name' : 'Askhat'}
# student.setdefault('address' , 'Западный Анар')
# print(student)

# Дз 7 
# def bibi():
#     user = input("Введите фразу: ")
#     user1 = user.split()
#     c = []
#     for word in user1:
#         c.append(word[0].upper())
#     d = "".join(c)
#     print(d)
# bibi()

#Дз 8 
#  def bibi():
#     bibi = "Money, money, money, it's always sunny, in the richmen's world".lower()
#     print("money:", bibi.count("money"))
#     print("it's:", bibi.count("it's"))
#     print("always:", bibi.count("always"))
#     print("sunny:", bibi.count("sunny"))
#     print("in:", bibi.count("in"))
#     print("the:", bibi.count("the"))
#     print("richmen's:", bibi.count("richmen's"))
#     print("world:", bibi.count("world"))
# bibi()

# Задача 9
# def isogram(word):
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "broke" 
# word2 = "drive"
# word3 = "fantastic"
# print(isogram(word1))  
# print(isogram(word2)) 
# print(isogram(word3))

# Задача 10
# def n(a):
#     a_n = int(str(a)[::-1])
#     print(a_n)
# n(27)

# ДОП Д/З
# def user(): 
#     while True:
#         user = input("Можете задать вопрос: ")
#         if user.find("?")>=0:
#             print("Конечно!")
#         elif user.find("!")>=0:
#             print("Успокойся")
#         elif user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# user()



























