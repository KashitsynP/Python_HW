# Задача 1 (арифметические выражения):
# вариант а:

# while True:
#     try:
#         s = input("Enter arithmetic expression (Enter 'q' fot exit): ")
#         if s == 'q':
#             print("Good bye!")
#             break
#         if '+' in s:
#             s = s.split('+')
#             print(int(s[0]) + int(s[1]))
#         elif '-' in s:
#             s = s.split('-')
#             print(int(s[0]) - int(s[1]))
#         elif '*' in s:
#             s = s.split('*')
#             print(int(s[0]) * int(s[1]))
#         elif '/' in s:
#             s = s.split('/')
#             print(int(s[0]) / int(s[1]))
#         else:
#             print("Error: Enter only '+, -, *, /' in arithmetic expression")
#     except (ZeroDivisionError, ValueError) as er:
#         print(er) 

# ------------------------------------

# вариант б (покороче):

# while True:
#     try:
#         s = input("Enter arithmetic expression (Enter 'q' fot exit): ")
#         if s == 'q':
#             print('Good bye!')
#             break
#         o = '+' if '+' in s else '-' if '-' in s else '*' if '*' in s else '/' if '/' in s else print("Error: Enter '+, -, *, /' in arithmetic expression")
#         s = s.split(o)
#         a = int(s[0])
#         b = int(s[1])
#         print(a + b if o == '+' else a - b if o == '-' else a * b if o == '*' else a / b)
#     except (ZeroDivisionError, ValueError, IndexError) as er:
#         print(er)

###########################################################################################

# Задача 2 (Подсчёт элементов в списке):

# from random import randint

# s = []
# cnt_neg, cnt_pos, cnt_zero = 0, 0, 0

# for i in range(20):
#     s.append(randint(-100, 100))
# print(s)
# print('Максимальное число:', max(s))
# print('Минимальное число:', min(s))
# for i in s:
#     if i < 0:
#         cnt_neg += 1
#     elif i > 0:
#         cnt_pos += 1
#     else:
#         cnt_zero +=1
# print('Колличество отрицательных:', cnt_neg)
# print('Колличество положительных:', cnt_pos)
# print('Колличество нулей:', cnt_zero)



