import random

def sum_digit(num):
    str_num = str(num)
    str_num = str_num.replace('.', '')
    my_list = list(str_num)
    my_list_num = map(int, my_list)
    s = sum(my_list_num)
    return s

def sum_digit_v2(num):
    str_num = str(num)
    str_num = str_num.replace('.', '')
    int_num = int(str_num)
    s = 0

    while int_num > 0:
        tepm = int_num % 10
        s += tepm
        int_num //= 10

    return s    

def my_factorial(num):
    res = 1

    for i in range(1, num +1):
        res *= i
        print(res, end= " ")

def sum_elements(num):
    lst_elem = []
    for i in range(1, num+1):
        lst_elem.append((1 + (1 / i))**i)

    print(lst_elem)      

    return lst_elem    

def generate_rnd_lst(num):
    new_lst = list()

    for i in range (num):
        new_lst.append(random.randint(-num, num))

    return new_lst    

def mult_elems(new_lst):
    pos = 0
    result = 1

    while pos != -1:
        pos = int(input("Введите номер позиции элемента в списке (нумерация начинается с 0, -1 - закончить ввод позиций): "))

        if 0 <= pos < len(new_lst):
            result *= new_lst[pos]
        else:
            if pos != -1:
                print("Такой позиции не существует!!!") 
    return result           

def shuffle_list(lst):
    new_list = list()
    base_len = len(lst)

    for i in range(base_len):
        temp_idx = random.randint(0, len(lst) - 1)
        new_list.append(lst[temp_idx])
        lst.pop(temp_idx)
    return new_list


while True:
    print("1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
    print("2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")
    print("3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.")
    print("4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .")
    print("5. Реализуйте алгоритм перемешивания списка.")
    menu_item = input("Выберите номер задачи: ")

    if menu_item == "1":

        number_one = float(input("Введите число: "))

        print(f"Сумма цифр числа {number_one} = {sum_digit(abs(number_one))}")

        print(f"V.2 Сумма цифр числа {number_one} = {sum_digit_v2(abs(number_one))}")        

    elif menu_item == "2":
        
        number_two = int(input("Введите число: "))

        my_factorial(number_two)

        print()

    elif menu_item == "3":

        number_three = int(input("Введите число: "))

        print(sum(sum_elements(number_three)))
        
    elif menu_item == "4":

        number_four = int(input("Введите число элементов: "))

        rnd_lst = generate_rnd_lst(number_four)

        print(f"Сгенерированный список: {rnd_lst}")

        print(f"Произведение элементов на указанных позициях = {mult_elems(rnd_lst)}")    

    elif menu_item == "5":

        base_lst = [5, 98, -4, -33, 12, 7, 65, 999, -1]

        print(f"Исходный список: {base_lst}")

        print(f"Перемешанный список: {shuffle_list(base_lst)}")

        
    elif menu_item == "0":
        break
    else:
        print("Вы ввели неправильное значение!")     


