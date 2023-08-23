# compare three numbers and show smallest and biggest number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is the biggest number")
    else:
        print(c, "is the biggest number")
else: 
    if b > c:
        print(b, "is the biggest number")
    else:
        print(c, "is the biggest number")