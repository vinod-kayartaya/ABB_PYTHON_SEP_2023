def main():
    nums = [12, 40, 289, 28, 59, 93, 922, 19, 69, 39]

    # create a new list of numbers from the `nums` but only even numbers
    even_nums = []
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)

    print(even_nums)

    # create a new list of numbers consisting only of odd numbers from `nums`
    # using list comprehension
    odd_nums = [n for n in nums if n % 2 == 1]
    print(odd_nums)

    # create a new list of numbers consisting of square of each number from `nums`
    square_nums = [n*n for n in nums]
    print(square_nums)


if __name__ == '__main__':
    main()
