first =input("Enter first number : ")
optr =input("Enter operator ")
second=input("Enter second number : ")

first=int(first)
second=int(second)

if optr == "+":
    print(first+second)
elif optr == "-":
    print(first-second)

elif optr == "/":
    print(first/second)
elif optr == "%":
    print(first%second)
else: 
    print("invaid operation")