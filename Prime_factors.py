x=int(input("Enter a number:"))
y=[]
if x==0:
    print("The number is neither prime nor composite")
elif x==1:
    print("The number is neither prime nor composite")
else:
    i=2
    while(x>0 and x>1):
        if x%i==0:
            y.append(i)
            x=x/i
        else:
            i=i+1
print(y)



