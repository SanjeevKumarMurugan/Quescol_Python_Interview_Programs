x=int(input("Enter a range:"))
if x==0:
    print("Please enter a positive integer")
elif x==1:
    print("Please enter x greater than 1")
else:
    for i in range(2,x+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)