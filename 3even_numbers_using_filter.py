def even_finder(num):
    return num%2==0

numbers=[0,1,2,3,4,5,6,7,8,9,10]

evens = list(filter(even_finder, numbers))

print(f"The list of even numbers is {evens}")