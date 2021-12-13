import json
with open('users.data', 'r') as f:
            users = []
            for line in f:
                users.append(list(line.rstrip().split(',')))
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
if func == '1':
    with open(name+'_balance.data', 'r') as f:
        amount = int((f.read()))
    print('your amount is:  ', amount)
if func == '3':
    with open('case.json', 'r') as f:
        str_case = json.load(f)
    case = dict((int(k),int(v)) for k,v in str_case.items())
    def display_stock():
        """ выводим наличие купюр по номиналу на экран"""
        # выводим на экран купюры доступные для выдачи
        in_stock = []
        for cell in case:
            if case[cell]>0:
                in_stock.append(cell)
        print('The banknotes with a nominals of ', in_stock, ' are available')
        return in_stock
    in_stock = request<=sum(i*j for i,j in case.items())
    def check_int():
        """проверяем на целочисленность"""
        while True:
            try:
                print('Enter the cash amount which is multiple by ', in_stock)
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
            print('Enter the cash amount which is multiple by ', in_stock[-1])
            return False
    check_pos = check_positive()
    def enough_money(request):
        """если предыдущие функции ок, то проверяем достаточность денег"""
        if check_positive!=False and request != False and request<=sum(i*j for i,j in case.items()):
            return True
        else:
            print('Not enough money in the cash mashine')
            return False 
    enough_mon = enough_money(request)
    print(request)
#    print(case)
#    request = 400
    def cash_machine(request):
        """алгоритм выдачи налички"""
        if check_pos!=False and enough_mon!=False and request != False and func == 3:
            cash = {} 
            for cell in case:
                if case[cell]<request//cell:
                    cash.update({cell: case[cell]})
                    request -= cell*case[cell]
#                    with open(name+'_transactions.json', 'a') as f:
#                        f.write(json.dumps('Cash taking  '+str(withdraw)))
                else:
                    cash.update({cell: request//cell})
                    case[cell]-=request//cell
                    request = request%cell
            stock = []        
            if request>0:
                print('Try amount which is multiple by ', stock[len(stock)-1])       
            print(request)
            print(case)
            return cash
#    cash = cash_machine(request)
#    print(cash)   
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

#if func == '5':
request = check_int()


