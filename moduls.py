# Модули - это Python файл
# В Python модули можно импортировать 3 способами 
# 1- импортировать сам модуль 
# import lesson8 # Без окончания  .py
# print(lesson8.hello())# вызываем функцию из модули lesson8
# print(lesson8.three_add(10, 10, 10))

# 2-импортировать отдельные определения из модуля 
# from lesson8 import hello
# print(hello())# вызываем функцию из другого модуля py 

# 3 - импортировать всё содержимое модуля сразу
# from lesson8 import * #оператор (*)означает все (весь)
# print(hello())
# print(three_add(5, 5, 5))
