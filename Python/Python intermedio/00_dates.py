# Dates (Fechas)

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

year_2026 = datetime(2026,1,1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second) 
    
print_date(now)

print_date(year_2026)

from datetime import time
current_time = time(10,52,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

day = date(2003,7,23)

print(day.year)
print(day.month)
print(day.day)

dif = year_2026 -now
print(dif)



