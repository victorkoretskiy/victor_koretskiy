# 3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів
# (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
# перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)
class LengthNameException(Exception): # создаём ошибки
    def __init__(self, length):
        self.length = length
class DigitPassException(Exception):
    def __init__(self, digit):
        self.digit = digit
class UpperPassException(Exception):
    def __init__(self, letter):
        self.letter = letter
def validate(name, password): # создаём функцию валидации
    try:
        if len(name) < 3 or len(name) > 50: # Проверяем длину имени
            raise LengthNameException(len(name))
        if len(password) < 8 or any(map(str.isdigit, password)) == False: # Проверяем пароль на длину и наличие цифр
            raise  DigitPassException(len(password))
        if any(map(str.isupper, password)) == False: # Проверяем на наличие заглавных букв
            raise UpperPassException(len(password))
        else: 
            print('Status - Ok') # если ни одно из условий не выполняется, выводим статус - ок
    except LengthNameException as err:
        print('name must to be in range(3,50)')
    except DigitPassException as err:
        print('password must to be longer than 8 symbol and consist of at least one digit')
    except UpperPassException as err:
        print('password must to be consist of at least one upper leter')
    return(name, password)
names = {'Vasya': '123456Vjk', 'Petya': '123', 'Kolya': 'kjV654321', 'Masha': 'dsdsjfhd321', 'Yu': 'dsdsghgV231'} # вводим словарь с данными пользователей
for i in names:           # проходим каждый элемент словаря функцией валидации
    print('_' * 20)               
    print('Name:', i, '  Password:', names[i]) # 
    validate(i, names[i])  
    
