#1. Програма-світлофор.
#  Створити програму-емулятор світлофора для авто і пішоходів.
# Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
# Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Green
#      Yellow     Green
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green
import time
def trafficlight(cycle):
    i=0
    while True:
        if i >=len(cycle):
            i=0
        yield cycle[i]
        i+=1
for condition in trafficlight([('Red', 'Green'), ('Red', 'Green'), ('Red', 'Green'), ('Red', 'Green'), ('Yellow', 'Green'), ('Yellow', 'Green'), ('Green', 'Red'), ('Green', 'Red'), ('Green', 'Red'), ('Green', 'Red'), ('Yellow', 'Red'), ('Yellow', 'Red')]):
    print(str(condition).replace("'",'').replace('(','').replace(')','').replace(',',''))
    time.sleep(1)
