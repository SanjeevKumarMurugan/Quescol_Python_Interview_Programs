x=input("Enter a number:")
y=x.split(",")
z=[int(i) for i in y]
avg=sum(z)/len(z)
print(int(avg))