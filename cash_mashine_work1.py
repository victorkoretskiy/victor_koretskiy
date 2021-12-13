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
if func == '3':
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
if func == '3':
    request = check_int()
def check_positive():
    """проверяем на >0 и кратность самой малой купюре в наличии"""
    if request is not False and request>0 and request%in_stock[-1] == 0:
        return True
    else:
        return False
if func == '3':
    check_request = check_positive()
def enough_money():
    """если предыдущие функции ок, то проверяем достаточность денег"""
    if check_request is True and request<=sum(i*j for i,j in case.items()):
        return True
    else:
        return False
if func == '3':
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
            print('Try amount which is multiple by ', stock[len(stock)-1])
#        print(request)
#        print(case)
        return cash
    else:
        return None
if func == '3':
    cash = cash_machine(request)
    print('Take your money', cash)
    #case = { k:int(case_init[k]) - int(cash[k]) for k in case_init if k in cash }
    #print(case)
if func == '2':
    while True:
        try:
            with open(name+'_balance.data', 'r') as f:
                amount = int((f.read()))
            fill = int(input('enter the amount you want to deposit into the account'))
            if fill<0:
                print('Enter the correct value')
            amount += fill
            with open(name+'_transactions.json', 'a') as f:
                f.write(json.dumps('The amount was filled by  '+str(fill)))
            with open(name+'_balance.data', 'w') as f:
                f.write(str(amount))
        except ValueError as err:
            print('Wrong value. Do you want to try once more? y/n)')
            answer = str(input())
            if answer == 'y':
                continue
            else:
                print('Wrong value. The program will be closed)')
        break                
if func == '4':
    print('The cash machine is closed')
def collector_mode():
    with open('case.json', 'r') as f:
        str_case = json.load(f)
    case = dict((int(k),int(v)) for k,v in str_case.items())
    print('Entering the collector mode, the initial case is: ', case)
    slot1 = int(input('enter the new qty of 1000-banknotes'))
    slot2 = int(input('enter the new qty of 500-banknotes'))
    slot3 = int(input('enter the new qty of 200-banknotes'))
    slot4 = int(input('enter the new qty of 100-banknotes'))
    slot5 = int(input('enter the new qty of 50-banknotes'))
    slot6 = int(input('enter the new qty of 20-banknotes'))
    slot7 = int(input('enter the new qty of 10-banknotes'))
    case = {1000: slot1, 500: slot2, 200: slot3, 100: slot4, 50: slot5, 20:slot6, 10: slot7}
    with open('case.json', 'w') as f:
        json.dump(case, f)
    return case
if func == '5':
    col = collector_mode()
    print(col)
if func == '1':
    with open(name+'_balance.data', 'r') as f:
        amount = int((f.read()))
    print('your amount is:  ', amount)
