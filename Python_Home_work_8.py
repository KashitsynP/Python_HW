# n1 = int(input("Start: "))
# n2 = int(input("End: "))
# for i in range(n1, n2 + 1):
#     if i % 7 == 0:
#         print(i)


n1 = int(input("Start: "))
n2 = int(input("End: "))
list = []
list_rev = []
list_seven = []
count_5 = 0
for i in range(n1, n2 + 1):
    list.insert(i, i)
    list_rev.insert(i, i)
    if i % 5 == 0 and i != 0:
        count_5 += 1
        if i % 7 == 0:
            list_seven.insert(i, i)
    elif i % 7 == 0 and i != 0:
        list_seven.insert(i, i)
list_rev.sort(reverse=True)
print()
print("All values: ", list)
print("All values reversed: ", list_rev)
print("Multiply 7: ", list_seven)
print("Count multiply 5: ", count_5)



# n1 = int(input("Start: "))
# n2 = int(input("End: "))
# for i in range(n1, n2 + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, " - Fizz Buzz")
#     elif i % 3 == 0:
#         print(i, " - Fizz")
#     elif i % 5 == 0:
#         print(i, " - Buzz")
#     else:
#         print(i)
