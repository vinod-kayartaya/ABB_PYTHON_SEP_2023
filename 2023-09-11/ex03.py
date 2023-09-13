'''
This is an example module for accepting an number 
representing the `year` and print if it is a valid year and also
a leap year or not.
'''

year = int(input('Enter a number representing year (1-9999): '))

if year < 1:
  print('You entered an invalid year.')
  print('Please retry with 1 to 9999')
  exit()

if year > 9999:
  print('You must enter an year equals to or before 9999')
  exit()

if (year % 400) == 0 or ((year % 4) ==0 and (year % 100) != 0):
  print(f'The year {year} is a leap year and has 366 days')
else:
  print(f'The year {year} is not a leap year and has only 365 days')
