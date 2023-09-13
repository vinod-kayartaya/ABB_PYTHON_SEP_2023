def main():
    nums = [12, 40, 289, 28, 59, 93, 922, 19, 69, 39]
    print(f'element at index 0 is {nums[0]}')
    print(f'the last element is {nums[len(nums)-1]}')
    print(f'the last element is {nums[-1]}')
    print(f'the element before the last element is {nums[-2]}')
    print(f'the element at index 4 is {nums[4]}')
    print(f'the elements between index 2 and 6 are {nums[2:7]}')
    print(f'elements upto index 7 are {nums[0:7]}')
    print(f'elements upto index 7 are {nums[:7]}')
    print(f'elements from index 4 till the end are {nums[4:]}')
    print(f'all elements in the list are {nums[:]}')
    print(f'all elements in the list are {nums[::]}')
    print(f'all elements in the list are {nums[::1]}')
    print(f'numbers at even indices are {nums[::2]}')
    print(f'numbers ate odd indices are {nums[1::2]}')
    print(f'all elements in the list are {nums[::-1]}')


if __name__ == '__main__':
    main()
