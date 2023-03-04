# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.

spisok = [1, 2, 3, 4, 5, 6, 7, 1, 3, 5, 7, 8, 9, 10]
spisok2 = []

for i in spisok:
    if i not in spisok2:
        spisok2.append(i)


print(spisok2)
print(len(spisok2))
