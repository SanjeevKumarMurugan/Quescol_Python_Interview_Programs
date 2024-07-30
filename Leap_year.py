x=int(input("Enter the year:"))
def is_leap(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
if is_leap(x)==True:
    print(f"{x} is leap year")
else:
    print(f"{x} is not leap year")
