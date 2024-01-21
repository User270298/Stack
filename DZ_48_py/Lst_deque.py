from collections import deque

lst = list(map(int, input('Input \n').split()))
print(lst)
dq = deque(lst)


def add():
    x = int(input('Add: '))
    if x in dq:
        print('Такое число уже есть в списке')
    else:
        dq.append(x)
        return dq


def remove():
    x = int(input('Remove: '))
    if not x in dq:
        print('Такого числа нет')
    while x in dq:
        dq.remove(x)

    return dq


def see_lst():
    x = int(input('Как хотите посмотреть список:'
                  '\n0- обычное отображение;\n1-реверсивное отображение\n'))
    if x == 0:
        return dq
    else:
        dq.reverse()
        return dq


def search():
    x = int(input('Найти элемент: '))
    if x in dq:
        return True
    return False


def switch():
    x = int(input('Какое значение изменить: '))
    if x in dq:
        z = int(input('На какое значение поменять: '))
        y = int(input('0-Заменить все вхождения\n'
                      '1-Заменить первое вхождение\n'))
        if y == 0:
            for i in range(len(dq)):
                if dq[i] == x:
                    dq.remove(dq[i])
                    dq.insert(i, z)
            return dq
        else:
            for i in range(len(dq)):
                if dq[i] == x:
                    dq.remove(dq[i])
                    dq.insert(i, z)
                    return dq
    else:
        print('Нет такого значения')


def main():
    x=-1
    while x!=0:
        x = int(input('Нажмите:\n1-Добавить элемент\n2-удалить элемент\n'
                      '3-посмотреть список\n4-найти элемент\n5-поменять элемент\n0-Выйти\n'))
        if x == 1:
            print(add())
        elif x == 2:
            print(remove())
        elif x == 3:
            print(see_lst())
        elif x == 4:
            print(search())
        elif x == 5:
            print(switch())

main()
