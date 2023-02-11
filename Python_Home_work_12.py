s = '\u066D'
p = ' '
while True:
    n = input("Enter letter 'а - к': ")
    match n:
        case 'а':
            for i in range(6, 0, -1):
                print(*p * (6 - i) + s * i)
        case 'б':
            for i in range(6, 0, -1):
                print(*(6 - i) * s)
        case 'в':
            for i in range(6):
                if i == 0:
                    print(*s * 5)
                elif i == 1:
                    print(p, *s * 3)
                elif i == 2:
                    print(p, p, s)
                else:
                    print(p)
        case 'г':
            for i in range(6):
                if i < 3:
                    print(p)
                elif i == 3:
                    print(p, p, s)
                elif i == 4:
                    print(p, *s * 3)
                else:
                    print(*s * 5)
        case 'д':
           for i in range(6):
                if i == 0 or i == 5:
                    print(*s * 5)
                elif i == 1 or i == 4:
                    print(p, *s * 3)
                else:
                    print(p, p, s)
        case 'е':
            for i in range(5):
                if i == 0 or i == 4:
                    print(s, p * 5, s)
                elif i == 1 or i == 3:
                    print(*s * 2, p, *s * 2)
                else:
                    print(*s * 5)
        case 'ж':
            for i in range(5):
                if i == 0 or i == 4:
                    print(s, p * 5)
                elif i == 1 or i == 3:
                    print(*s * 2, p)
                else:
                    print(*s * 3)
        case 'з':
            for i in range(5):
                if i == 0 or i == 4:
                    print(p * 5, s)
                elif i == 1 or i == 3:
                    print(p, p, *s * 2)
                else:
                    print(p, *s * 3)
        case 'и':
            for i in range(6, 0, -1):
                print(*s*i)
        case 'к':
            for i in range(6):
                print(*(p * (6 - i)) + s * i)
        case _:
            print("Enter only 'a - к'!")
            

    