#Lucky number

n = int(input("Enter the number"))
small = 9
smallest = 9
while n>0:
    rem = int(n%10)
    n = int(n/10)
    if rem < small:
        small = smallest
        smallest = rem
print("2nd smallest is",small)