# Задача 1 (Проверка на полиндром)

# line = input("Enter string: ")
# line = line.lower().split(" ")
# line = "".join(line)

# if (line == line[::-1]):
#     print("Слово - полиндром")
# else:
#     print("Не полиндром")

#----------------------------------------------------------------------------------

# Задача 2 (Замена зарезервированных слов в тексте на верхний регистр)

# s1 = input("Enter text: ")
# s2 = input("Enter the reserved words: ").split()
# for i in s2:
#     s1 = s1.replace(i, i.upper())
# print(s1)

#----------------------------------------------------------------------------------

# Задача 3 (Подсчёт предложений в тексте)

# s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# s = s.replace(".", "|").replace("!", "|").replace("?", "|")
# arrS = s.split("|")
# print(len(arrS) - 1)
