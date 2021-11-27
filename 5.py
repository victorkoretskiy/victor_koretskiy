# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fibonacci(n):
    a1 = a2 = 1
    fib =[]
    while a2 < n:
        fib.append(a2)
        a1, a2 = a2, a1 + a2
    return fib
    
 
