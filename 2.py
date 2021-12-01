# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - щось своє :)(своє: пароль повинен мати хоча б одну заглавну літеру)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
class LengthNameException(Exception):
    def __init__(self, length):
        self.length = length
class DigitPassException(Exception):
    def __init__(self, digit):
        self.digit = digit
class UpperPassException(Exception):
    def __init__(self, letter):
        self.letter = letter        
def validate(name, password):
    try:
        if len(name) < 3 or len(name) > 50:
            raise LengthNameException(len(name))
        if len(password) < 8 or any(map(str.isdigit, password)) == False:
            raise  DigitPassException(len(password))
        if any(map(str.isupper, password)) == False:
            raise UpperPassException(len(password))
    except LengthNameException as err:
        print('name must to be in range(3,50)')
    except DigitPassException as err:
        print('password must to be longer than 8 symbol and consist of at least one digit')
    except UpperPassException as err:
        print('password must to be consist of at least one upper leter')
    return(name, password)
        
    
