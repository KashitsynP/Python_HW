# Задание 1

from math import sqrt
n1 = int(input("Enter start range: "))
n2 = int(input("Enter end range: "))
list = []
count = 0
for i in range(n1, n2 + 1):
    if i <= 1:
        continue
    for j in list:
        if j > (int(sqrt(i) + 1)):
            list.append(i)
            count += 1
            break
        if (i % j == 0):
            break
    else:
        list.append(i)
        count += 1
print("Prime numbers: ", list)
print("Count of prime numbers: ", count)

# -------------------------------------------------

# Задание 2

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

# -------------------------------------------------

# Задание 3

# n1 = int(input("Enter start range: "))
# n2 = int(input("Enter end range: "))
# for i in range(n1, n2 + 1):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

