# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
first_year = int(input())
last_year = int(input())
for i in range(first_year, last_year):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        print(i)
