number=int(input("Enter the number upto which You want primes numbers: "))

def primes(number):
    primes=[]
    for i in range(1,number+1):
        count=0
        
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        
        if count==2:
            primes.append(i)
    
    return primes

a=primes(number)
print(f'The prime numbers upto {number} is {a}')
