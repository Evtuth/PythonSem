# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте

stroka = str(input('Введите ваш текст: '))

array = stroka.split()

print(array)
print(len(array))



