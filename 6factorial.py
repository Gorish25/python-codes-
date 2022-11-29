num=int(input("Enter the number upto which you want factorial"))

factorial = 1

if num<0:
    print("Sorry the factorial does not exist ")
elif num==0:
    print("The factorial of 0 is always 1")
else:
    for i in range(1,num+1):
        factorial*=i

print(f'The factorial of {num} is {factorial}')