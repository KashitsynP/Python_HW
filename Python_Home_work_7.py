# n = int(input("Введите число от 1 до 100: "))
# print("Fizz Buzz" if (n % 3 == 0 and n % 5 == 0) else "Buzz" if (n % 5 == 0) else "Fizz" if (n % 3 == 0) else n if (0 < n <= 100) else "Error: incorrect value")


# n = int(input("Введите число: "))
# m = int(input("Возвести в степень от 0 до 7: "))
# match m:
#     case 0:
#         print(n**0)
#     case 1: 
#         print(n**1)
#     case 2: 
#         print(n**2)
#     case 3: 
#         print(n**3)
#     case 4: 
#         print(n**4)
#     case 5: 
#         print(n**5)
#     case 6: 
#         print(n**6)
#     case 7: 
#         print(n**7)
#     case _:
#         print("Error: incorrect value")


# print("Выберите оператора: ")
# print("1. МТС → МТС")
# print("2. МТС → Мегафон")
# print("3. Мегафон → Мегафон")
# print("4. Мегафон → МТС")
# op = int(input(">>>> "))

# print("Введите время разговора (мин): ")
# time = float(input(">>>> "))

# price1 = 1.5
# price2 = 2.5
# price3 = 1.6
# price4 = 2.1

# print("Стоимость разговора: ", time * price1 if (op == 1) else price2 if (op == 2) else price3 if (op ==3) else price4 if (op == 4) else "Error: incorrect operator")

# match op:
#     case 1:
#         print("Стоимость разговора: ", price1 * time, "руб.")
#     case 2:
#         print("Стоимость разговора: ", price2 * time, "руб.")
#     case 3:
#         print("Стоимость разговора: ", price3 * time, "руб.")
#     case 4:
#         print("Стоимость разговора: ", price4 * time, "руб.")
#     case _:
#         print("Error: incorrect operator")




# print("Продажи менеджеров, $:")
# m1 = int(input("Михаил: "))
# m2 = int(input("Николай: "))
# m3 = int(input("Максим: "))

# salary1 = 200 + (m1 * 0.03 if (m1 < 500) else m1 * 0.05 if (500 <= m1 < 1000) else m1 * 0.08)
# salary2 = 200 + (m2 * 0.03 if (m2 < 500) else m2 * 0.05 if (500 <= m2 < 1000) else m2 * 0.08)
# salary3 = 200 + (m3 * 0.03 if (m3 < 500) else m3 * 0.05 if (500 <= m3 < 1000) else m3 * 0.08)

# bonus1 = 200 if m1 > m2 and m1 > m3 else 0
# bonus2 = 200 if m2 > m1 and m2 > m3 else 0
# bonus3 = 200 if m3 > m2 and m3 > m1 else 0

# print("")
# print(("Михаил - лучший менеджер месяца!") if m1 > m2 and m1 > m3 else ("Николай - лучший менеджер месяца!") if m2 > m1 and m2 > m3 else ("Максим - лучший менеджер месяца!") if m3 > m1 and m3 > m2 else "В этом месяце нет победителей")
# print("Зарплата:")
# print("Михаил: ", salary1 + bonus1, "$")
# print("Николай: ", salary2 + bonus2, "$")
# print("Максим: ", salary3 + bonus3, "$")
