# . Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
def count(a):
    if a > 0:
        result = a**2
    if a < 0:
        result = a+100
    if a == 0:
        result = a
    return result
