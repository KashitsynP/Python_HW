# n1 = int(input("Введите 1-е число: "))
# n2 = int(input("Введите 2-е число: "))
# n3 = int(input("Введите 3-е число: "))
# choise = input("Введите + или *: ")
# if choise == "+":
#     print(n1 + n2 + n3)
# elif choise == "*":
#     print(n1 * n2 * n3)
# else:
#     print("Error: Неверный знак")


n1 = int(input("Введите 1-е число: "))
n2 = int(input("Введите 2-е число: "))
n3 = int(input("Введите 3-е число: "))

choise = int(input("1 - min, 2 - max, 3 - среднеарифметическое: "))
if choise == 1:
    if n1 <= n2 <= n3:
        print(n1)
    elif n2 <= n1 <= n3:
        print(n2)
    else:
        print(n3)
    print(min(n1, n2, n3))
elif choise == 2:
    if n1 >= n2 >= n3:
        print(n1)
    elif n2 >= n1 >= n3:
        print(n2)
    else:
        print(n3)
    print(max(n1, n2, n3))
elif choise == 3:
    print((n1 + n2 + n3) / 3)
else:
    print("Error: Неверный знак")


# n = float(input("Сколько метров? - "))
# choise = int(input("1 - мили, 2 - дюймы, 3 - ярды: "))
# # miles = n * 0.00062
# # inch = n * 39.37
# # yard = n * 1.09
# if choise == 1:
#     print(float(n * 0.00062))
# elif choise == 2:
#     print(float(n * 39.37))
# elif choise == 3:
#     print(float(n * 1.09))
# else:
#     print("Error: Неверный знак")

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end="\t")
#     print("\n")

# n = [1, 2, 3, 4, 5]
# print(n[0], n[1], n[2], n[3], n[4], sep='')
# n.reverse()
# # for j in n[::-1]:
# #     print(j)
# print(n[0], n[1], n[2], n[3], n[4], sep='')
    
