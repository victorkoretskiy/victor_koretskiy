import json
with open('users.data', 'r') as f:
            users = []
            for line in f:
                users.append(list(line.rstrip().split(',')))
with open('case.json', 'r') as f:
        str_case = json.load(f)
case = dict((int(k),int(v)) for k,v in str_case.items())
class RequestExceptionErr(Exception):
    pass
class LoginException(Exception):
    def __init__(self, user_login):
        self.user_login = user_login
def sign_in():
    names = dict(users)
    attempts = 3
    for i in range(attempts):
        try:
            name = str(input('Enter username '))
            password = str(input('Enter password '))
            login = (name, password)
            if login in names.items():
                return name
            if login not in names.items():
                raise LoginException('LogErr')
        except LoginException as err:
            print('Wrong login or Password')
            if i < attempts - 1:
                print('you used', i+1, 'of', attempts, 'attempts')
                continue
            else:
                print('Login Err after 3 attempts, the program will be closed')
        break
name = sign_in()
print(name)
class MenuException(Exception):
    pass
def main_menu():
    if name is not None:
        print('Greetings, ', name)
        while True:
            try:
                paragraphs = '1234'
                print('type 1 to check amount')
                print('type 2 to top up an account')
                print('type 3 to take cash')
                print('type 4 to exit')
                if name == 'Vasya':
                    paragraphs = '12345'
                    print("type 5 to enter the collector's mode")
                func = str(input('please, select an action'))
                if func in paragraphs:
                    return func
                else:
                    raise MenuException('MenuErr')
            except MenuException as err:
                print('Wrong menu function. Do you want to try once more? (y/n)')
                answer = str(input())
                if answer == 'y':
                    continue
                else:
                    print('wrong function, try again later')
            break
func = main_menu()
print(func)
def display_stock():
    """ выводим наличие купюр по номиналу на экран"""
    # выводим на экран купюры доступные для выдачи
    in_stock = []
    for cell in case:
        if case[cell]>0:
            in_stock.append(cell)
    print('The banknotes with a nominals of ', in_stock, ' are available')
    return in_stock
in_stock = display_stock()
def check_int():
    """проверяем на целочисленность"""
    while True:
        try:
            print('Enter the cash amount which is multiple by ', in_stock[-1])
            request = int(input())
            return request
        except ValueError as err:
            print('Wrong value. Do you want to try once more? y/n)')
            answer = str(input())
            if answer == 'y':
                continue
            else:
                print('Wrong value. The program will be closed)')
            return False
        break
request = check_int()
def check_positive():
    """проверяем на >0 и кратность самой малой купюре в наличии"""
    if request is not False and request>0 and request%in_stock[-1] == 0:
        return True
    else:
        return False
check_request = check_positive()
def enough_money():
    """если предыдущие функции ок, то проверяем достаточность денег"""
    if check_request is True and request<=sum(i*j for i,j in case.items()):
        return True
    else:
        return False
check_done = enough_money()
def cash_machine(request):
    """алгоритм выдачи налички"""
    if check_done == True:
        cash = {} 
        for cell in case:
            if case[cell]<request//cell:
                cash.update({cell: case[cell]})
                request -= cell*case[cell]
            else:
                cash.update({cell: request//cell})
                case[cell]-=request//cell
                request = request%cell
        stock = []        
        if request>0:
            for cell in case:
                if cell>=request and case[cell]>0:
                    stock.append(cell)
            print('Try amount which is multiple by ', stock[-1])
#        print(request)
#        print(case)
        return cash
if func == '3':
    print(cash_machine(request))

