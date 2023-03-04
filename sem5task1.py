# Требуется найти N-е число Фибоначчи

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

f = int(input('Введите число Фибоначи, которое хотите получить: '))

print(fib(f))