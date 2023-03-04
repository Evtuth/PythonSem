# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.

a = int(input('Введите целое неотрицательное число:'))
pred = 0
tek = 1
temp = None
count = 1
while pred <= a:
    count +=1
    if a == pred:
        print(count)
        break
    temp = pred
    pred = tek + pred
    tek = temp
else:
    print(-1)


