def square(num):
    return num**2

numbers=[1,2,3,4,5,6,7,8,9,10]

a=list(map(square, numbers))
print(f'The squares of values {numbers} is {a}')