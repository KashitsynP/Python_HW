# Задание 1:

# def degree():
#     while True:
#         x = input('Enter number or enter "q" to exit: ')
#         if (x == "q"):
#             print("Good bye!")
#             break
#         else:
#             y = input("Enter degree: ")
#             print(int(x)**int(y))
# degree()

# ---------------------------------------------------------
    
# Задание 2:

# count = 0
# for i in range(100, 1000):
#     n1, n2, n3 = str(i)
#     count += 1 if n1 == n2 or n1 == n3 or n2 == n3 else 0
# print(count)

# ---------------------------------------------------------
    
# Задание 3:

# count = 0
# for i in range(100, 1000):
#     n1, n2, n3 = str(i)
#     count += 1 if not(n1 == n2 or n1 == n3 or n2 == n3) else 0
# for i in range(1000, 10000):
#     n1, n2, n3, n4 = str(i)
#     count += 1 if not((n1 == n2 or n1 == n3 or n1 == n4) or (n2 == n3 or n2 == n4) or n3 == n4) else 0
# print(count)

# ---------------------------------------------------------
    
# Задание 4:

# while True:
#     n = input("Enter number (Enter 'q' for exit): ")
#     if n == 'q':
#         print("Good bye!")
#         break
#     else: 
#         if not n.isdigit():
#             print("Error: you must enter number!")
#         else:
#             n = n.replace('3', '')
#             n = n.replace('6', '')
#             print(n)


