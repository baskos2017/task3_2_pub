"""Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу додавати у створений список на початку. Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8."""


def my_order()->list:
    """Функція додає замовлення користувача(кортеж товар кількість одиниць) до списку замовлень"""
    my_orderall.insert(0, quantity_of_goods)
    return my_orderall

def count_off_goods()->int:
    """Створюється глобальна  змінна в  яку записується кількість одиниць  товату по кожній позиції магазину яку потім використовує  інша функція для додавання товару до списку замовлень"""
    global count
    count = int(input('Введіть кількість:'))
    return count

all_goods = [
    'pen',
    'pencil',
    'notebook',
    'paper',
    'folder',
    'paper clip',
    'file'
]

my_orderall = []

quantity_of_goods = ()

while True:
    print('Виберіть товар')
    sellect = input('1 - pen \n2 - pencil\n3 - notebook\n4 - paper \n5 - folder\n6 - paper clip\n7 - file\n8 - Вихід\n')

    if sellect == '1':
        count_off_goods()
        quantity_of_goods = ('pen', count)
        my_order()
    elif sellect == '2':
        count_off_goods()
        quantity_of_goods = ('pencil', count)
        my_order()
    elif sellect == '3':
        count_off_goods()
        quantity_of_goods = ('notebook', count)
        my_order()
    elif sellect == '4':
        count_off_goods()
        quantity_of_goods = ('paper', count)
        my_order()
    elif sellect == '5':
        count_off_goods()
        quantity_of_goods = ('folder', count)
        my_order()
        count_off_goods()
    elif sellect == '6':
        count_off_goods()
        quantity_of_goods = ('paper clip', count)
        my_order()
    elif sellect == '7':
        count_off_goods()
        quantity_of_goods = ('file', count)
        my_order()
    elif sellect == '8':
        break

print(my_orderall)
