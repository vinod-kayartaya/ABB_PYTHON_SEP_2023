# print(f'ex06 is under execution and the value of __name__ is {__name__}')

from vin_utils import max_days_in_year

def give_max(num1, num2):
    return num1 if num1 > num2 else num2
    
def main():
    year = int(input('Enter a year (e.g, 2023): '))
    max_days = max_days_in_year(year)
    print(f'The year {year} has {max_days} days.')

    max_days = max_days_in_year()
    print(f'the current year has {max_days} days')

if __name__ == '__main__':
    main()
