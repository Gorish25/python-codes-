numbers=[1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda num:num**2, numbers))

print(f'The square of numbers {numbers} is {square}')

evens = list(filter(lambda num:num%2==0, numbers))

print(f'The even numbers in the list are {evens}')