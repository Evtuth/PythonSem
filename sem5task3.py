# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

num = int(input('Введите число: '))

def easy_num(num):
    for i in range(2, num):
        if num%i != 0:
            print('Число не простое')
            break
    else:
        if num == 0 or num == 1:
            print('Число не натуральное') 
        else:
            print('Число простое')

easy_num(num)