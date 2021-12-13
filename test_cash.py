import json
func = '3'
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
            print('Enter the cash amount which is multiple by ', in_stock[-1])
            return False
    check_pos = check_positive()
    #print(check_pos)
    def enough_money(request):
        """если предыдущие функции ок, то проверяем достаточность денег"""
        if check_positive!=False and request != False and request<=sum(i*j for i,j in case.items()):
            return True
        else:
            print('Not enough money in the cash mashine')
            return False 
    enough_mon = enough_money(request)
    #print(enough_mon)
    #print(check_pos)
    #print(request)
    #print(func)
    def check_done():
        if check_pos!=False and enough_mon!=False and request != False:
            return True
        else:
            return False
    def cash_machine(request):
        """алгоритм выдачи налички"""
        if check_done == True:
            cash = {}
            for cell in case:
                if case[cell]<request//cell:
                    cash.update({cell: case[cell]})
                    request -= cell*case[cell]
                    print(request)
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
    print(cash_machine(request))  
