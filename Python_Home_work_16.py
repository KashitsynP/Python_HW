# Задание 1
# def printText():
#     print('''"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\n\t\t\t\t\tBill Gates''')
# printText()

#--------------------------------------------------------------

# Задание 2
# def printEven(a, b):
#     for i in range(a + 1, b):
#         if i % 2 == 0:
#             print(i)
# printEven(-11, 11)

#--------------------------------------------------------------

# Задание 3

# def paintSquare(a, symbol, boolean):
#     # Рисует в консоли квадрат, в зависимости от введенных параметров
#     #    a     → сторона квадрата
#     # symbol   → символ для отображения 
#     # boolean: → True - заполненный квадрат
#     #          → False - пустой квадрат
#     if boolean == False:
#         for i in range(a):
#             if i == 0 or i == (a - 1):
#                 print(symbol * a)
#             else:
#                 print(symbol + ' ' * (a - 2) + symbol)
#     if boolean == True:
#         for i in range(a):
#             print(symbol * a)

# paintSquare(20, '-', False)

#--------------------------------------------------------------

# Задание 4

# def minOfNum(a, b, c, d, e):
#     # Возвращает минимальное значение из введенных чисел
#     return min(a, b, c, d, e)
# print(minOfNum(5, 1, 12, 6, 3))

#--------------------------------------------------------------

# Задание 5

# def multiAB(a, b):
#     # Возвращает произведение чисел в заданном диапазоне
#     # a → нижняя граница
#     # b → верхняя граница
#     result = 1
#     # Если границы диапазона перепутаны, следующее условие меняет местами переменные
#     if a > b:
#         a, b = b, a
#     if a < b:
#         for i in range(a, b + 1):
#             result *= i
#     return result
# print(multiAB(5, 1))

#--------------------------------------------------------------

# Задание 6

# def countOfNum(a):
#     # Возвращает колличество цифр в числе
#     return len(str(a))
# print(countOfNum(3452))

#--------------------------------------------------------------

# Задание 7

# def isPalindrom(num):
#     # Проверка числа на палиндром
#     # num: целочисленное
#     # Возвращает: True  → палиндром
#     #             False → не палиндром
#     num_str = str(num)
#     return True if (num_str == num_str[::-1]) else False
# print(isPalindrom(22322))
