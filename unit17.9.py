integer_num = input('Введите целые числа через пробел: ')
user_num = int(input('Введите любое число: '))
Error = 'Ошибка ввода'

def is_int(str):      # для определения цифр в строке
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in integer_num:   # проверка правильности введенных данных.
    print(Error, ': Отсутствуют пробелы между цифровыми значениями')
    integer_num = input('Введите целые числа через пробел: ')
if not is_int(integer_num):
    print(Error, ': Ведено не цифровое значение или не целые числа')
    integer_num = input('Введите целые числа через пробел: ')
else:
    integer_num = integer_num.split()
list_integer_num = [int(item) for item in integer_num] # замена списка строк на числа

def merge_sort(L):                  # Сортировка списка
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
list_integer_num = merge_sort(list_integer_num)

def binary_search(array, element, left, right): # алгоритм двоичного поиска для установки позиции элемента
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Введено число вне диапазона списка!!! ' \
               'Повторите операцию сначала'

print(f'Список чисел по возрастанию: {list_integer_num}')
# Устанавливаем номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

if not binary_search(list_integer_num, user_num, 0, len(list_integer_num)):
    rI = min(list_integer_num, key=lambda x: (abs(x - user_num), x))
    ind = list_integer_num.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_num:
        print(f'''Введенное число отсутствует в списке \nБлижайшее к нему меньшее число {rI} с индексом {ind} \nБлижайшее к нему большее число {list_integer_num[max_ind]} с индексом {max_ind}''')
    elif rI > user_num:
        print(f'''Введенное число отсутствует в списке \nБлижайшее к нему большее число {rI} с индексом {list_integer_num.index(rI)} \nБлижайшее к нему меньшее число {list_integer_num[min_ind]} с индексом {min_ind}''')
    elif min_ind < 0:
        print(f'''Введенное число отсутствует в списке \nБлижайшее к нему большее число {rI} с индексом {list_integer_num.index(rI)} \nМеньшее число отсутствует в списке''')
    elif list_integer_num.index(rI) == 0:
        print(f'Индекс введенного числа: {list_integer_num.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_integer_num, user_num, 0, len(list_integer_num))}')
