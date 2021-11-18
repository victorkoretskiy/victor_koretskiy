a = []
n = int(input('введите количество строк (N): '))
for i in range(n):
    line = input('введите строку ')
    a = [str(k) for k in line]
print(a)
