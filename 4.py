n = int(input('введите количество строк (N): '))
print('введите', n, 'строк через запятую и пробел')
a = input().split(', ')
b = a[:n]
print("".join(b))
