# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def custom_range(start, stop, step = 1):
    if start != None and stop == None:
        temp = start
        start = 0
        stop = temp
    if start < stop and step < 0:
        print([])
    if start > stop and step >0:
        print([]) 
    if step > 0 and start < stop:
        while start !=stop:
            yield start + step
            start += step
    if step < 0 and start > stop:
         while start !=stop:
            step = abs(step)
            yield start - step
            start -= step            
for i in custom_range(20, 4, -2):
    print(i)

