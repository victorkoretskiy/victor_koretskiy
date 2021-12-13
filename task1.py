def start():
    with open('users.data', 'r') as f:
        users = []
        for line in f:
            users.append(list(line.rstrip().split(',')))
    class LoginException(Exception):
        def __init__(self, user_login):
            self.user_login = user_login
    def log_in(name, password):
        names = dict(users)
        login = (name, password)
        while True:
            try:
                if login in names.items():
                    result = name
                if login not in names.items() and silent == False:
                    raise LoginException('LogErr')
            except LoginException as err:
                result = print('Wrong login or Password')
            return result
    input_name = str(input('Enter username'))
    input_pass = str(input('Enter password'))
    name = log_in(input_name, input_pass)
    print('Hello', name)
    import json
    def operations(name):
        print('type 1 - to check amount')
        print('type 2 - to top up an account')
        print('type 3 - to take cash')
        print('type 4 to exit')
        func = str(input())
        fill = 0
        withdraw = 0
        with open(name+'_balance.data', 'r') as f:
            amount = int((f.read()))
        if func == '1':
            print('your amount is:  ', amount)
        if func == '2':
            fill = int(input('enter the amount you want to deposit into the account'))
            amount += fill
            
            with open(name+'_transactions.json', 'a') as f:
                f.write(json.dumps('The amount was filled by  '+str(fill)))
        if func == '3':
            withdraw = int(input('enter the amount you want to withdraw from the account'))
            if amount < withdraw:
                print('Not enough money')
            else:    
                amount -= withdraw
            with open(name+'_transactions.json', 'a') as f:
                f.write(json.dumps('Cash taking  '+str(withdraw)))
        with open(name+'_balance.data', 'w') as f:
            f.write(str(amount))
        return [func, fill, withdraw]
    print(operations(name))


