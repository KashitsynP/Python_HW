def bubble_sort_up(iList):
    # Function to sort the list in ascending order 
    for i in range(len(iList)):
        for j in range(len(iList) - 1, 0, -1):
            if (iList[j] < iList[j-1]):
                iList[j], iList[j-1] = iList[j-1], iList[j]
    return iList

def bubble_sort_down(iList):
    # Function to sort the list in descending order
    for i in range(len(iList)):
        for j in range(len(iList) - 1, 0, -1):
            if (iList[j] > iList[j-1]):
                iList[j], iList[j-1] = iList[j-1], iList[j]
    return iList


def binear(a, n):
    # Function for bineary search of index of value n
    # a → list
    # n → searching value
    l = 0
    r = len(a)-1
    cnt2 = 0
    while l <= r:
        mid = (l + r) // 2  
        cnt2 += 1
        if a[mid] == n:
            print(f'\nКолличество итераций в binear: {cnt2}')
            return f'Индекс числа {a[mid]}: {mid}'
        elif (a[mid] < n) if a[0] > a[1] else (a[mid] > n):
            r = mid - 1
        else:
            l = mid + 1
    return -1

def linear(a, n):
    # Function for linear search of index of value n
    # a → list
    # n → searching value
    cnt1 = 0
    for i in range(len(a)):
        cnt1 += 1
        if (a[i] == n):
            print(f'\nКолличество итераций в linear: {cnt1}')
            return f'Индекс числа {a[i]}: {i}'
    return -1

