x=int(input("Enter a number:"))
y=len(str(x))
num=x
sum=0
for i in range(y):
    digit=x%10
    sum=sum+digit**3
    x=x//10
if sum==num:
    print("The number is armstrong")
else:
    print("The number is not armtrong")