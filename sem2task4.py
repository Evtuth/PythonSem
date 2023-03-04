# n - число арбузов
# найти минимум и максимум веса

n = int(input('Введите число арбузов: '))
max = 0
min = 10000000
for i in range(n):
    ves_arbyz = int(input())
    if ves_arbyz < min:
        min = ves_arbyz
    if ves_arbyz > max:
        max = ves_arbyz
print(max, min)