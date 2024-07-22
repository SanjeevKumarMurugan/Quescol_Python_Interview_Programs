x=int(input("Enter number1:"))
y=int(input("Enter number2:"))
z=int(input("Enter number3:"))
if x>y and x >z:
    print(x,"is greatest")
elif y>z and y>x:
    print(y,"is greatest")
else:
    print(z,"is greatest")