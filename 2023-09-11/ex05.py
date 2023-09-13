# import vin_utils
from vin_utils import author_email, author_name, is_leap

# print(f'Author\'s name is {vin_utils.author_name} and their email is {vin_utils.author_email}')
print(f'Author\'s name is {author_name} and their email is {author_email}')

year = int(input('Enter a year (e.g, 2023): '))

# print(vin_utils.is_leap(year))
print(is_leap(year))