x=int(input("Enter a number:"))
y=[]
for i in range(1,x):
    if x%i==0:
        y.append(i)
if sum(y)==x:
    print(y)
    print("The number is perfect")
else:
    print(y)
    print("The number is not perfect")