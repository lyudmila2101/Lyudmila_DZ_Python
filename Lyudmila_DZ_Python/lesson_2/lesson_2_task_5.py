def month_to_season(month):
    if 2 < month <= 5:
        return('Весна')
    elif 5 < month <= 8:
        return('Лето')
    elif 8 < month <= 11:
        return('Осень')
    elif month == 12 or 0 < month <=3:
        return('Зима')
    else:
        return('Некорректный номер месяца')
    
month = int(input("Введите номер месяца (1-12):"))    
print (month_to_season(month))