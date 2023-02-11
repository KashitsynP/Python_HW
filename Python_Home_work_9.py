# Задача 1
# 
# n1 = int(input("Enter first num: "))
# n2 = int(input("Enter second num: "))
# sumEven = sumOdd = sumMultiNine = 0
# countEven = countOdd = countMultinine = 0

# for i in range(n1, n2 + 1):
#     if i % 9 == 0:
#         sumMultiNine += i
#         countMultinine += 1
#     if i % 2 == 0:
#         sumEven += i
#         countEven += 1
#     else:
#         sumOdd += i
#         countOdd += 1
           
# print(f"Summ Even: {sumEven}, Ariеthmetic mean: {sumEven/countEven}")
# print(f"Summ Odd: {sumOdd}, Ariеthmetic mean: {sumOdd/countOdd}")
# print(f"Summ Multiply 9: {sumMultiNine}, Ariеthmetic mean: {sumMultiNine/countMultinine if countMultinine != 0 else 0}")
        
# ----------------------------------------------------------------------------------------------------------------------
# 
# Задача 2  (Решил поэкспериментировать с функциями)
# 
# def line():
#     while True:
#         l = int(input("Enter the line length: "))
#         s = input("Enter symbol: ")
#         if s.isalnum():
#             print("Error! Введите символ!")
#         else:
#             for i in range(l):
#                 print(s)
#             break
# line()

# ----------------------------------------------------------------------------------------------------------------------

# Задача 3

def recognizeNumber():
    while True:
        n = int(input('Enter number (Don`t touch "7"): '))
        if n == 7:
            print("I told you so! Good Bye!")
            break
        elif n > 0:
            print("Number is positive")
        elif n < 0:
            print("Number is negative")
        else:
            print("Number is equal to zero")
recognizeNumber()

# ----------------------------------------------------------------------------------------------------------------------

# Задача 4

# def superfunc():
#     n = int(input("Enter number: "))
#     sum = max = min = n
#     print(f"Summ: {sum}, max: {max}, min: {min}")
#     while n != 7:
#         n = int(input("Enter number: "))
#         sum += n
#         if n > max:
#             max = n
#         elif n < min:
#             min = n
#         print(f"Summ: {sum}, max: {max}, min: {min}")
#     print("Good bye!")
# superfunc()






