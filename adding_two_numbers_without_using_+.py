def add_numbers(x,y):
    while y!=0:
        temp=x&y
        x=x^y
        y=temp<<1
    return x
a=10
b=20
print(add_numbers(a,b))