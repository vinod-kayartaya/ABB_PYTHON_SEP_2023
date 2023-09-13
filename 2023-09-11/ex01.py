# this is an example for testing different ways of printing

n1 = 10
n2 = 20

total = n1 + n2

print('the sum of', n1, 'and', n2, 'is', total)
print('the sum of ' + str(n1) + ' and ' + str(n2) + ' is ' + str(total))
print('the sum of %d and %d is %d' % (n1, n2, total))
print(f'the sum of {n1} and {n2} is {total}')
