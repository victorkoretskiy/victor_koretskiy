group = list(input('введите группу значений запятую с пробелом  ').split(", "))
n = input('введите символ для проверки')
for i in [group]:
    if n in i:
        print('True')
    else:
        print('False')
