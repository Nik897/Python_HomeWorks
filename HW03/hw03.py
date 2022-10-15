import math

def convert_str_in_lst():
    inp_data = input("Введите список чисел через пробел: ")
    my_list = list(inp_data.split())
    return my_list

def count_odd_pos(my_lst):
    sum = 0
    for i in range(1, len(my_lst), 2):
        sum += int(my_lst[i])
    return sum    

def couple_multi(my_lst):
    res_lst = list()
    for i in range(math.ceil(len(my_lst)/2)):
        res_lst.append(int(my_lst[i]) * int(my_lst[-1 - i]))
    return res_lst    

def difference_min_max(my_lst):
    min_flt = float(my_lst[0]) % 1
    max_flt = float(my_lst[0]) % 1

    for i in my_lst:
        fractional_part = float(i) % 1

        if fractional_part != 0:
            if fractional_part < min_flt:
                min_flt = fractional_part  
            elif fractional_part > max_flt:
                max_flt = fractional_part
    return max_flt - min_flt       

def decimal_in_binary(num):
    res_bin = ""
    while num > 0:
        temp = num % 2
        res_bin = str(temp) + res_bin
        num //= 2
    return res_bin    

def fib(num):
    if num in [1, 2]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)    

def neg_fib(num):
    if num == -1:
        return 1
    elif num == -2:
        return -1
    else:
        return neg_fib(num + 2) - neg_fib(num + 1)        



while True:
    print("1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")
    print("2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
    print("3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
    print("4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")
    print("5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

    menu_item = input("Выберите номер задачи: ")

    if menu_item == "1":
        
        my_list_1 = convert_str_in_lst()

        print(f"Сумма элементов на нечетных позициях = {count_odd_pos(my_list_1)}")      

    elif menu_item == "2":

        my_list_2 = convert_str_in_lst()
        
        print(f"Произведение пар чисел: {couple_multi(my_list_2)}")

    
    elif menu_item == "3":

        my_list_3 = convert_str_in_lst()

        print(f"Разница между максимальным и минимальным значением дробной части элементов = {difference_min_max(my_list_3)}")
        
    elif menu_item == "4":

        number = int(input("Введите число: "))

        print(decimal_in_binary(number))

    elif menu_item == "5":

        fib_list = [0]    
        number_fib = int(input("Введите число: "))

        for i in range(1, number_fib + 1):
            fib_list.append(fib(i))

        for i in range(1, number_fib + 1):
            fib_list.insert(0, neg_fib(-i))    

        print(fib_list)    

    elif menu_item == "0":
        break
    else:
        print("Вы ввели неправильное значение!")     