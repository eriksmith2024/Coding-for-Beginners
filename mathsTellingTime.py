from datetime import datetime 

today = datetime.today()
print('\nToday is:', today )

print()

for attr in \
['year','month','day','hour','minute','second','microsecond']:
    print( attr, ':\t', getattr(today, attr))

print('\nTime:', today.hour, ':',today.minute, sep = '')

day = today.strftime( '%A' )
month = today.strftime( '%B')

print('\nDate:', day, month,today.day, '\n')

today = today.replace(year=2023)

print('\nDate:', day, month, today.day, today.year, '\n')
