# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
a = ''
def my_func(a):
    num = ''
    alp = ''
    if 30 <= len(a) <= 50:
        for char in a:
            if char.isdigit():
                num = num + char
            if char.isalpha():
                alp = alp + char
        result = print('char:',len(a), '  num:', len(num), '  alpha:', len(alp))
    if len(a) < 30:
        total = 0
        for char in a:
            if char.isalpha():
                alp = alp + char
            if char.isdigit():
                num = num + char
                for i in num:
                    i = i.split()
                    for n in i:
                        total = total + int(n)
        result = (total, alp)
    if len(a) > 50:
        result = print('нет фантазии')
    return(result)
