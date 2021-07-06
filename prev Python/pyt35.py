n=int(input('Enter no.'))
c=0
if n>1:
    for i in range(2,n+1):
        if(n%i==0):
            c=c+1
    if(c==1):
        print("prime")
    else:
        print("not prime")
else:
    print("not a prime number")
