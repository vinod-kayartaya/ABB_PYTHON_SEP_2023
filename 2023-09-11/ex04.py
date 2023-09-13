'''
This script is an example for accepting month/year from the user
and find the number of days in it.
'''

year = int(input('Enter a year (e.g, 2023): '))
if year < 1 or year > 9999:
    print('Year must be between 1 and 9999')
    exit()

month = int(input('Enter a month (e.g, 9): '))
if 1 <= month <= 12:
    if month == 2:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            print(f'There are 29 days in {month}/{year}')
        else:
            print(f'There are 28 days in {month}/{year}')
    elif month in (4, 6, 9, 11):
        print(f'There are 30 days in {month}/{year}')
    else:
        print(f'There are 31 days in {month}/{year}')
else:
    print('Month must be between 1 and 12')