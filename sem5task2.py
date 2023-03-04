# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.

n = int(input('Введите количество оценок: '))

spisok = []

for i in range(0, n):
    spisok.append(int(input('Введите оценку от 1 до 5: ')))

print(spisok)

max = 0

for i in spisok:
    if i > max:
        max = i

min = max

for i in spisok:
    if i < min:
        min = i

for i in range(0, len(spisok)):
    if spisok[i] == max:
        spisok[i] = min

print(spisok)