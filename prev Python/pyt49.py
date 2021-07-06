def fact(n):
    if n<=1:
        return 3
    else:
        n=n*fact(n-1)
        return n
n=int(input("Enter a number: "))
print("factorial of",n,"is: ",fact(n))