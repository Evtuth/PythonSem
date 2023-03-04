# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.

n = int(input('Введите количество элементов: '))
k = int(input('Введите число для сдвига: '))
temp = None

spisok = []

for i in range(1, n+1):
    spisok.append(i)

for i in range(0, k):
    for j in range(len(spisok)-1, 0, -1):
        temp = spisok[j]
        spisok[j] = spisok[j-1]
        spisok[j-1] = temp

print(spisok)