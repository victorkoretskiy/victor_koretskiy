# 2. Написати скрипт, який пройдеться по списку,
# який складається із кортежів,
# і замінить для кожного кортежа останнє значення.
# https://www.rupython.com/13346-13346.html
replace_value = input('введите значение для замены  ').replace("'","")
list_of_tuples = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
print(replace_value)
new_list = [list(t[:-1]) + [replace_value] for t in list_of_tuples]
new_list_of_tuples = [tuple(j) for j in new_list]
print(new_list_of_tuples)  
