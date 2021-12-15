class LoginException(Exception):
    pass
class MenuException(Exception):
    pass
import json
import time
def sign_in():
    with open('users.data', 'r') as f:
        users = []
        for line in f:
            users.append(list(line.rstrip().split(',')))
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
def main_menu(name):
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
def display_amount(name):
    """пункт меню 1"""
    with open(name+'_balance.data', 'r') as f:
        amount = int((f.read()))
        print('your amount is:  ', amount) 
def change_amount(name):
    """пункт меню 2"""
    while True:
        try:
            with open(name+'_balance.data', 'r') as f:
                amount = int((f.read()))
            fill = int(input('enter the amount you want to deposit into the account'))
            if fill<0:
                print('Enter the correct value')
            amount += fill
            with open(name+'_transactions.json', 'a') as f:
                f.write(json.dumps('The amount was filled by  '+str(fill)+'  '+str(time.ctime())))
            with open(name+'_balance.data', 'w') as f:
                f.write(str(amount))
        except ValueError as err:
            print('Wrong value. Do you want to try once more? y/n)')
            answer = str(input())
            if answer == 'y':
                continue
            else:
                print('returning to the main menu')
        break                
def take_cash(name):
    """пункт меню 3"""
    def take_case():
        """вызываем накопитель банкомата"""
        with open('case.json', 'r') as f:
            str_case = json.load(f)
        case = dict((int(k),int(v)) for k,v in str_case.items())
        return case
    case = take_case()
    def display_stock(case):
        """выводим наличие купюр по номиналу на экран"""
        stock = []
        for cell in case:
            if case[cell]>0:
                stock.append(cell)
        print('The banknotes with a nominals of ', stock, ' are available')
        return stock
    stock = display_stock(case) 
    def check_request():
        """проверяем запрос выдачи налички на валидность"""
        while True:
            try:
                request = int(input('Please, enter the amount'))
                with open(name+'_balance.data', 'r') as f:
                    amount = int((f.read()))
                if request > sum(i*j for i,j in case.items()):
                    print('Not anough money. Try another amount? y/n')
                    answer = str(input())
                    if answer == 'y':
                        continue
                    else:
                        return None
                        print('The program is closed')
                if request <= 0 or request%stock[-1]>0 and request%50>0:
                    print('Please type the amount which is multiple by',
                          stock[-1], 'Try another amount? y/n')
                    answer = str(input())
                    if answer == 'y':
                        continue
                    else:
                        return None
                        print('The program is closed')
                if request > amount:
                    print('Not enough money on your account. Try another amount? y/n')
                    answer = str(input())
                    if answer == 'y':
                        continue
                    else:
                        return None               
                else:
                    return request
            except ValueError as err:
                print('Please, type correct value. Try once more? y/n)')
                answer = str(input())
                if answer == 'y':
                    continue
                else:
                    return None
                    print('The program is closed')       
            break
    request = check_request()
    def cash_machine(request):
        """алгоритм выдачи налички"""
        case_init = case
        cash = {}
        request_init = request
        if (request%100)%20 == 0 and case.get(10) == 0:
            case.pop(50)
        for cell in case:
            if case[cell]<request//cell:
                cash.update({cell: case[cell]})
                request -= cell*case[cell]                
            else:
                cash.update({cell: request//cell})
                case[cell]-=request//cell
                request = request%cell
        if request!=0:
            print('Try another amount, recomended: ', request_init - request)
        else:
            case_init = { k:int(case_init[k]) - int(cash[k]) for k in case_init if k in cash }
            cash_final = {}
            for cell in cash:
                if cash[cell] != 0:
                    cash_final.update({cell: cash[cell]})
            print('Take your money', cash_final)           
            with open(name+'_balance.data', 'r') as f:
                init_amount = int((f.read()))
            amount = init_amount - sum(i*j for i,j in cash_final.items())
            with open(name+'_balance.data', 'w') as f:
                f.write(str(amount))
            with open(name+'_transactions.json', 'a') as f:
                f.write(json.dumps('Take out cash  '+str(sum(i*j for i,j in \
                                cash_final.items()))+'  '+str(time.ctime())))
            with open('case.json', 'w') as f:
                json.dump(case, f)
        return cash_final
    return cash_machine(request)   
def collector_mode():
    """пункт меню 5"""
    with open('case.json', 'r') as f:
        str_case = json.load(f)
    case = dict((int(k),int(v)) for k,v in str_case.items())
    print('Entering the collector mode, the initial case is:')
    print(case)
    for cell in case:
        print('To load the new case, please define quantities of banknotes in cells')
        print('Enter the qty of ', cell)
        case[cell] = input()
    with open('case.json', 'w') as f:
        json.dump(case, f)
    print('the case has been loaded')
    print(case)
def start():
    name = sign_in()
    while True:
        func = main_menu(name)
        if func =='1':
            display_amount(name)
            answer = input('take another action(y - main menu, any key - exit)')
            if answer == 'y':
                continue
            else:
                break
        if func == '2':
            change_amount(name)
            answer = input('take another action(y - main menu, any key - exit)')
            if answer == 'y':
                continue
            else:
                break
        if func == '3':
            take_cash(name)
            answer = input('take another action(y - main menu, any key - exit)')
            if answer == 'y':
                continue
            else:
                break
        if func == '4':
            break
        if func == '5':
            collector_mode()
            answer = input('take another action(y - main menu, any key - exit)')
            if answer == 'y':
                continue
            else:
                break
        else:
            continue
print(start())


        
    
