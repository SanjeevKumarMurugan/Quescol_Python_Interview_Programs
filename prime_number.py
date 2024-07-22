x=int(input("Enter a number:"))
if x==0:
    print(x,"is neither prime nor composite")
elif x==1:
    print(x,"is not prime")
else:
    for i in range(2,x):
        if x%i==0:
            print(x,"is not a prime number")
            break
    else:
        print(x,"is a prime number")

#Another approach which uses less iteration

'''
x = int(input("Enter a number: "))
if x <= 1:
    print(x, "is neither prime nor composite")
elif x == 2:
    print(x, "is a prime number")
else:
    is_prime = True
    # Check divisibility from 2 to sqrt(x)
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number")
        '''