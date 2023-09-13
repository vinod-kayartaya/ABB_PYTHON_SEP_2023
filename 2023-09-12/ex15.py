def convert_to_float(str_num):
    try:
        return float(str_num)
    except ValueError:
        return None


def main():
    str_nums = input('Enter a bunch of numbers separated by one space: ')
    nums = str_nums.split()
    nums = [convert_to_float(n) for n in nums]

    sqr_nums = [None if n is None else n*n for n in nums ]
    print(nums)
    print(sqr_nums)


if __name__ == '__main__':
    main()
