from math import pi, e


def my_func(atr:int = 1):
    """ якась муть """
    print('atr', atr)

step = 5
count = int(input('Введите количество повторов:'))
print(step * count)
print(pi * step * count)
print(e * 2)
while count >= 0:
    count -= 1
my_str = 'my string'
my_sum = 0
for elem in my_str:
   my_sum += pow(my_str.find(elem), 2)
print("sum = ", my_sum)
print(my_func(atr=5))