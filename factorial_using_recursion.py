x=int(input("Enter a number:"))
# fact=1
# for i in range(1,x+1):
#     fact=fact*i
# print(fact)
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(x))