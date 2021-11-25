# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
def season(month):
    calendar = {'winter':(12, 1, 2), 'spring':(3, 4, 5), 'summer':(6, 7, 8), 'autumn':(9, 10, 11)}
    for s in calendar:
        if month in calendar[s]:
            result = s
    return(result)
