# функции 2 часть
# def geeks(name):
#     print("Привет", name)
# geeks("Bibi")

# # Встроенные функции - print, len, input
# print("Geeks Pro")
# print(len("nurbolot"))
# print(len([10, 20, 30, 90]))
# print("Number: ")

# def input(num1, num2):
#     print(num1+num2)
# input(20, 40)

# def mult(num1:int, num2:int)-> int:
#     "Это умножение двух чисел"
#     print(num1 * num2)
# mult(5, 15)
# mult(20.01, 5.0)

# def reverse_name(name:str="kurmanbek") -> str:
#     "Функция которая переворачивает строку вашего имени"
#     print(name[::-1])
# reverse_name()

# def chet_nechet(number:int=1) -> str:
#     "Функция получает аргументв виде int и выдает числа четное или нечетное число"
#     if number % 2 == 0:
#         return "Chet"
#     else:
#         return "Nechet"
# print(chet_nechet())
# print(chet_nechet(10))

# def add(num1:int=1, num2:int=1)-> int:
#     return num1 + num2

# def sub(num1:int=1, num2:int=1)-> int:
#     return num1 - num2

# def mult(num1:int=1, num2:int=1)-> int:
#     return num1 * num2

# def div(num1:int=1, num2:int=1)-> float:
#     return num1 / num2

# def main(number1:int=1, number2:int=1, operator:str="+")-> int:
#     if operator == "+":
#        return add(number1, number2)
#     elif operator == "-":
#         return sub(number1, number2)
#     elif operator == "*":
#         return mult(number1, number2)
#     elif operator == "/":
#         return div(number1, number2)
#     else:
#         return "Такого оператора нету"
    
# print(main(10, 30,"+"))
# print(main(30, 20,"-"))
# print(main(10, 5,"*"))
# print(main(10, 10,"/"))

def hello():
    return "Hello world"

def three_add(num1, num2, num3):
    return num1 * num2 * num3