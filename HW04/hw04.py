from decimal import Decimal
from random import randint
import decimal

def accuracy(num):
    res = 0
    while num < 1:
        res += 1
        num *= 10
    return res

def my_pi(num):
    res = Decimal(0)

    decimal.getcontext().prec = num + 1

    i = 0
    while i < num:
        res += (Decimal(1) / (16**i))*((Decimal(4) / (8*i + 1)) -
                                     (Decimal(2) / (8*i + 4))-(Decimal(1) / (8*i + 5))-(Decimal(1) / (8*i + 6)))
        i += 1
    return res


def simple_multiplier(spl_num, num):
    result = []
    for i in range(len(spl_num)):
        if num % spl_num[i] == 0:
            result.append(spl_num[i])
    return result


def simple_number(num):
    simple_lst = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_lst.append(i)
    return simple_lst


def no_double_numbers(my_str):
    result = []
    for i in range(len(my_str)):
        flag = True
        for j in range(len(my_str)):
            if i != j:
                if my_str[i] == my_str[j]:
                    flag = False
        if flag:
            result.append(my_str[i])
    return result


# def empty_list(num):
#     result = []
#     for i in range(num + 1):
#         result.append(0)
#     return result


def generate_coefficients(num):
    res = []
    for i in range(num + 1):
        res.append(randint(-100, 101))
    return res


def polynomial(coeff_lst, num):
    res_str = "=0"
    for i in range(num+1):
        if coeff_lst[i]:
            if coeff_lst[i] > 0:
                if i == 0:
                    res_str = "+" + str(coeff_lst[i]) + res_str
                elif i == 1:
                    res_str = "+" + str(coeff_lst[i]) + "x" + res_str
                else:
                    res_str = "+" + str(coeff_lst[i]) + "x^" + str(i) + res_str
            else:
                if i == 0:
                    res_str = str(coeff_lst[i]) + res_str
                elif i == 1:
                    res_str = str(coeff_lst[i]) + "x" + res_str
                else:
                    res_str = str(coeff_lst[i]) + "x^" + str(i) + res_str

    if res_str[0] == "+":
        return res_str[1:]
    else:
        return res_str


while True:
    print("1. Вычислить число Пи c заданной точностью d (d от 0.1 до 0.0000000001)")
    print("2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
    print("3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.")
    print("4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k")
    print("5. ")

    menu_item = input("Выберите номер задачи: ")

    if menu_item == "1":

        number_1 = float(input("Введите точность числа (от 0.1 до 0.0000000001): "))

        acc = accuracy(number_1)

        print(my_pi(acc))

    elif menu_item == "2":

        number_2 = int(input("Введите натуральное число (> 0): "))

        if number_2 > 0:

            s = simple_number(number_2)

            new_s = simple_multiplier(s, number_2)

            print(f"Простые множители числа {number_2} -> {new_s}")

        else:
            print("Вы ввели некорректное число!!!")

    elif menu_item == "3":

        my_string = input("Введите последовательность цифр: ")

        print(no_double_numbers(my_string))

    elif menu_item == "4":

        k = int(input("Задайте натуральную степень: "))

        coefficients = generate_coefficients(k)

        s = polynomial(coefficients, k)

        print(f"Данный результат записан в файл 'polynominal_4.txt' {s}")

        my_file = open("polynominal_4.txt", "a")

        my_file.write(s + "\n")

        my_file.close()

    elif menu_item == "5":

        print(1)

    elif menu_item == "0":
        break
    else:
        print("Вы ввели неправильное значение!")
