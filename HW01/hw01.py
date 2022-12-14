# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Введте чмсло от 1 до 7, обозначающее день недели:"))

# if 0 < day < 8:
#     if (day == 6 or day ==7):
#         print("Это выходной")
#     else:
#         print("Это рабочий день")
# else:
#     print("Такого дня недели не существует!!!")


# ------------------------------------------------------------------------------------------------------------------
# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x or y or z) == (not x and not y and not z):
#                 print(f"{x} {y} {z} -> 1")
#             else:
#                 print(f"{x} {y} {z} -> 0")


# --------------------------------------------------------------------------------------------------
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input("Введите координату X: "))
# y = int(input("Введите координату Y: "))

# if (x != 0 and y != 0):
#     if x > 0 and y > 0:
#         print(f"точка ({x}, {y}) находится в 1й четверти")
#     elif x < 0 and y > 0:
#         print(f"точка ({x}, {y}) находится во 2й четверти")
#     elif x < 0 and y < 0:
#         print(f"точка ({x}, {y}) находится в 3й четверти")
#     elif x > 0 and y < 0:
#         print(f"точка ({x}, {y}) находится в 4й четверти")
# else:
#     print("Координаты X и Y не должны равняться 0!")


# --------------------------------------------------------------------------------------------------------
# # 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quter = int(input("Введите номер четверти (1-4): "))

# if 0 < quter < 5:
#     if quter == 1:
#         print("x > 0, y > 0")
#     elif quter == 2:
#         print("x < 0, y > 0")
#     elif quter == 3:
#         print("x < 0, y < 0")
#     elif quter == 4:
#         print("x > 0, y < 0")
# else:
#     print("Такой четверти не существует!")


# -------------------------------------------------------------------------------------------------------------
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

first_point = input(
    "Введите координаты X Y первой точки  через пробел: ").split()
second_point = input(
    "Введите координаты X Y второй точки через пробел: ").split()

distanse = math.sqrt((int(second_point[0])-int(first_point[0]))
                     ** 2 + (int(second_point[1])-int(first_point[1]))**2)

print(f"Расстояние между точками = {distanse}")
