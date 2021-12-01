#1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
 #  Логіка наступна:
  #     якщо введено коректну пару ім'я/пароль - вертається <True>;
   #    якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
    def __init__(self, user_login):
        self.user_login = user_login
def log_in(name, password, silent = False):
    names = {'Vasya': 1234, 'Petya': 123, 'Kolya': 4321, 'Masha': 321, 'Lena': 231}
    login = (name, password)
    try:
        if login in names.items():
            result = True
        if login not in names.items() and silent == True:
            result = False
        if login not in names.items() and silent == False:
            raise LoginException('LogErr')
    except LoginException as err:
        result = print('Wrong login or Password')
    return result

