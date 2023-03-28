## DATES ##

from datetime import datetime # agrupa fecha y hora

now = datetime.now()

print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)


timestamp = now.timestamp()

def print_date(date):
    print (date.year)
    print (date.month)
    print (date.day)
    print (date.hour)
    print (date.minute)
    print (date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 3, 28) # Mínimo para definir un año: año, mes, día

print_date(year_2023)


from datetime import time  # agrupa solo hora
current_time = time()
print(current_time.hour)
print(current_time.min)
print(current_time.second)


from datetime import date  # agrupa solo fecha
current_date = date(2022,10,6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

from datetime import timedelta # trabajar con franjas de fechas

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print ( end_timedelta - start_timedelta)                         
print ( end_timedelta + start_timedelta)
