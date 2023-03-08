# Задание 1

"""Необходимо отсортировать первые две трети списка
в порядке возрастания, если среднее арифметическое
всех элементов больше нуля; иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить
в обратном порядке."""

# lst = [5, 6, 8, 9, 2, 3, 4, 7, 1]

# len = len(lst)
# mean = sum(lst) / len
# one_thirds = int(len // 3)
# two_thirds = int(len // 1.5)

# def sort_list(lst):
#     lst_res, lst_end = [], []
#     if mean > 0:
#         for i in (lst[:two_thirds]):
#             lst_res.append(i)
#         for i in (lst[two_thirds:]):
#             lst_end.append(i)
#     else:
#         for i in (lst[:one_thirds]):
#             lst_res.append(i)
#         for i in (lst[one_thirds:]):
#             lst_end.append(i)
#     lst_res.sort()
#     lst_end.reverse()
#     lst_res += lst_end
#     return lst_res
# print(sort_list(lst))

###########################################################################################

# Задание 2

"""Написать программу «успеваемость». Пользователь
вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
меню для пользователя:
■ Вывод оценок (вывод содержимого списка);
■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
■ Выходит ли стипендия (стипендия выходит, если
средний бал не ниже 10.7);
■ Вывод отсортированного списка оценок: по возрастанию или убыванию."""


# import operator
# def progress(list):
#     print("\n----------Журнал успеваемости студента----------")
#     while True:
#         try:
#             list = [int(input("Введите оценки студента (от 1 до 12): ")) for el in range(10)]
#         except ValueError or TypeError:
#             print("Error! Ошибка ввода. Введите оценки заново.")
#             continue
#         for i in list:
#                 if i < 1 or i > 12:
#                     print(f'\nError!!! Оценка "{i}" должна быть от 1 до 12')
#                 break
    
#         dict_progress = {}
#         for i in range(len(list)):
#             dict_progress[i+1] = list[i]
#         while True:
#             while True:
#                 print("Оценки:", dict(dict_progress))
#                 print("Желаете изменить оценку?")
#                 user_choise = int(input("1 - да\n2 - нет, продолжить\n>>>> "))
#                 if user_choise != 1:
#                     break
#                 if user_choise == 1:
#                     print("\nВведите номер предмета для замены оценки: ")
#                     choise_key = int(input(">>>> "))
#                     print("Введите оценку: ")
#                     choise_value = int(input(">>>> "))
#                 if (choise_value < 1) or (choise_value > 12):
#                     print(f'\nError! Оценка "{choise_value}" должна быть от 1 до 12')
#                     break
                    
#                 if (choise_key < 1) or (choise_key > 10):
#                     print("\nТакого предмета нет\n")
#                     break
#                 dict_progress = dict(dict_progress)
#                 dict_progress.update({choise_key:choise_value})
#                 print("Измененные оценки:", dict_progress)
#             print("\nСтипендия:", True if sum(dict(dict_progress).values())/10 >= 10.7 else False)
#             print("\nВывод списка оценок: \n1 - по возрастанию\n2 - по убыванию")
#             choise_sort = int(input(">>>> "))
#             dict_progress = sorted(dict(dict_progress).items(), key=operator.itemgetter(1), reverse=(False if choise_sort == 1 else True))
#             print(dict(dict_progress))
#             print("Чтобы выйти нажмите 'Enter', чтобы продолжить - '1'")
#             n = input(">>>> ")
#             if n == '1':
#                 continue
#             else:
#                 break 
#         break
# progress(list)
###########################################################################################

# Задание 3

"""Написать программу, реализующую сортировку списка
методом усовершенствованной сортировки пузырьковым
методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
это количество равно нулю, то продолжать сортировку
нет смысла — список отсортирован."""

def superBubbleSort(l):
    n = len(l)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                new_n = i
        n = new_n
        if n == 0:
            break
    return l

print(superBubbleSort([9, 8, 7, 6, 5, 0, 3, 2, 1, 0]))
