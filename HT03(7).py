# 7.калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
def count(x, sign, y):
    x = float(x)
    y = float(y)
    s = sign
    if s in ('+', '-', '*', '/'):
        if s == '+':
            result = x + y
        elif s == '-':
            result = x - y 
        elif s == '*':
            result = x * y
        elif s == '/':
            if y != 0:
                result = x / y
            else:
                result = print("division by zero")
        else: result = print('wrong sign')
    return result


