author_name = 'Vinod Kumar Kayartaya'
author_email = 'vinod@vinod.co'


def is_leap(year):
    '''
    this method accepts a year as an argument or parameter and returns True or False
    based on if the year is leap or not
    '''
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def max_days_in_year(year=2023):
    '''
    this method returns 366 or 365 based on whether the input year is a leap year or not.
    if the year is not supplied as argument, then 2023 will be assumed.
    '''
    return 366 if is_leap(year) else 365


def is_prime(number):
    if number <= 1: return False

    divisor = 2
    limit = number // 2

    while divisor <= limit:
        if number % divisor == 0:
            return False
        divisor += 1
    
    return True


def factorial(num):
    if num <= 1:
        return 1
    
    f = 1
    for n in range(2, num+1):
        f *= n # f = f * n

    return f


def line(char='-', size=80):
    print(char*size)

    
def reverse(text):
    # rev = ''
    # for ch in text:
    #     rev = ch + rev 
    # return rev
    return text[::-1]

def reverse_by_words(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)


def dirr(obj):
    return [a for a in dir(obj) if not a.startswith('_')]