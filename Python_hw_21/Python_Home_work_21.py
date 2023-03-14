"""                 Задание 1
Есть четыре списка целых. Необходимо их объединить
в пятом списке. Полученный результат в зависимости от
выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием линейного поиска.
"""

# Import custom module sortfind.py

import sortfind

# l1 = [5, 6, 1, 9]
# l2 = [90, 60, 20, 70]
# l3 = [12, 18, 11, 0]
# l4 = [111, 115, 101, 999]

# def joinLists():
#     # Function return index of user input value from list
#     # Concatenation and print lists
#     l5 = l1 + l2 + l3 + l4
#     print("\nОбъединенный список:")
#     print(l5)
#     while True:
#         # Use functions from import module to sort list l5
#         print("\nОтсотрировать:\n1 - по возрастанию\n2 - по убыванию")
#         choise1 = input(">>>> ")
#         if choise1 == '1':
#             sortfind.bubble_sort_up(l5)
#         elif choise1 == '2':
#             sortfind.bubble_sort_down(l5)
#         else:
#             print("Error! Ошибка ввода!")
#             continue
#         while True:
#             print("\nОтсотрированный список: ")
#             print(l5)
#             # Use function from import module to find and print index of value
#             print("\nВведите искомое значение: ")
#             choise2 = int(input('>>>> '))
#             if choise2 not in l5:
#                 print("\nТакого значения нет в списке\n")
#                 continue
#             else:
#                 return sortfind.linear(l5, choise2)

# print(joinLists())

###############################################################################

"""                Задание 2
Есть четыре списка целых. Необходимо объединить
в пятом списке только те элементы, которые уникальны
для каждого списка. Полученный результат в зависимости
от выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием бинарного поиска.
"""

# l1 = [5, 6, 1, 9]
# l2 = [6, 7, 8, 9]
# l3 = [0, 1, 3, 4]
# l4 = [2, 3, 0, 10]

# def joinListsUnique():
#     # Function return index of user value from unique list of values
#     # Using the set function create a list of unique values
#     s = list(set(l1 + l2 + l3 + l4))
#     while True:
#         # Sort the list according to the user`s choise. Use functions from import module
#         print("\nОтсотрировать:\n1 - по возрастанию\n2 - по убыванию")
#         choise1 = input(">>>> ")
#         if choise1 == '1':
#             sortfind.bubble_sort_up(s)
#         elif choise1 == '2':
#             sortfind.bubble_sort_down(s)
#         else:
#             print("Error! Ошибка ввода!\n")
#             continue
#         while True:
#             print(f'\n{s}')
#             print("\nВведите искомое значение:")
#             choise2 = int(input('>>>> '))
#             # Use function binear search from import module to find index of user value
#             if choise2 not in s:
#                 print("\nТакого значения нет в списке\n")
#                 continue
#             else:
#                 return sortfind.binear(s, choise2)
    
# print(joinListsUnique())


