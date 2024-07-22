x=int(input("Enter the limit:"))
n1=0
n2=1
if x==0:
    print(n1)
elif x==1:
    print(n1)
    print(n2)
else:
    for i in range(x):
        n=n1+n2
        print(n1)
        n1=n2
        n2=n
