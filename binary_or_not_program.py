x=int(input("Enter a number:"))
for i in range(len(str(x))):
    j=x%10
    if j!=0 and j!=1:
        print("The number is not binary")
        break
else:
    print("The number is binary")