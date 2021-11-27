# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і
# кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.for num in range(2,101):
def prime_list(a, z):
    lst = []
    for n in range(a,z):
        if all(n%i!=0 for i in range(2,n)):
           lst.append(n)
    return lst
