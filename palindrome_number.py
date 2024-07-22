x=int(input("Enter a number:"))
y=str(x)
if x== int(y[::-1]):
    print("The number is palindrome")
else:
    print("The number is not palindrome")