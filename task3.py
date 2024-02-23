"""Програма інженерний калькулятор з використанням модуля math, в якому передбачене меню."""


from math import sin, tan, cos, sqrt


num = float(input("Введіть число:\n"))
sellect = input('1 - Обчислити синус \n2 - Обчислити тангенс\n3 - Обчислити косинус\n4 - Обчислити квадратний корінь\n')

if sellect == "1":
    print(sin(num))
if sellect == "2":
    print(tan(num))
if sellect == "3":
    print(cos(num))
if sellect == "4":
    print(sqrt(num))
