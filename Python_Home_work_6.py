# n = int(input("Введите цифру дня недели (1-7): "))
# if n == 1:
#     print("Понедельник")
# elif n == 2:
#     print("Вторник")
# elif n == 3:
#     print("Среда")    
# elif n == 4:
#     print("Четверг")
# elif n == 5:
#     print("Пятница")
# elif n == 6:
#     print("Суббота")
# elif n == 7:
#     print("Воскресенье")
# else:
#     print("Error: incorrect number")                


# n = int(input("Введите цифру месяца (1-12): "))
# if n == 1:
#     print("Январь")
# elif n == 2:
#     print("Февраль")
# elif n == 3:
#     print("Март")    
# elif n == 4:
#     print("Апрель")
# elif n == 5:
#     print("Май")
# elif n == 6:
#     print("Июнь")
# elif n == 7:
#     print("Июль")
# elif n == 8:
#     print("Август")
# elif n == 9:
#     print("Сентябрь")
# elif n == 10:
#     print("Октябрь")
# elif n == 11:
#     print("Ноябрь")
# elif n == 12:
#     print("Декабрь")
# else:
#     print("Error: incorrect number")


# n = int(input("Введите любое целое число: "))
# if n > 0:
#     print("Number is positive")
# elif n < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")


n1 = int(input("Введите 1-е число: "))
n2 = int(input("Введите 2-е число: "))
if n1 == n2:
    print("Числа равны")
elif n1 > n2:
    print(n2, n1, sep=", ")
else:
    print(n1, n2, sep=", ")
